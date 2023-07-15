from django.conf import settings
from rest_framework.response import Response
import csv, datetime, os, json, uuid

def custom_id():
    """generates 8 character alphanumeric ID """
    
    # unique_id = secrets.token_urlsafe(8)
    unique_id = str(uuid.uuid4())[:8]
    return unique_id

# Returns errors encountered while serialization
def get_validation_errors(serializer) -> dict:
    """Input: instance of DRF Serializer"""

    errors = {}
    for field_name, field_errors in serializer.errors.items():
        errors[field_name] = list(field_errors)
    return errors



# ToDo: Refactor and test properly. Add validations.

def get_export_filepath(subpath = "", file_prefix = "file", file_ext = "txt"):
    """Returns the filepath for extacting the files"""

    API_EXPORT_DIR = getattr(settings, "API_EXPORT_DIR", "AppData/API/Exports/")
    today = str(datetime.datetime.today()).replace(":",".")
    date, time = today.split(" ")
    export_path = "{}/{}".format(API_EXPORT_DIR, date)
    
    if subpath:
        export_path = "{}/{}/".format(export_path, subpath.strip('/'))
    
    export_path = export_path.replace("//", '/')
    filename = f"{file_prefix}_{today}.{file_ext.strip('.')}"

    if not os.path.isdir(export_path):
        os.makedirs(export_path)

    export_filepath = "{}/{}".format(export_path, filename.strip('/'))
    return filename, export_filepath



def export_taskboard(json_obj)->tuple:
    """input: json object"""
    try:
        COL_COUNT = 20
        task_list = []
        rm_fields = ("board_id", "team_id", "user_id",)

        task_list.append([" "] * COL_COUNT)

        board_tasks = json_obj.pop("board_tasks", None)
        board_details = json_obj

        board_name = board_details.get("name", "board")

        board_header = list(board_details.keys())
        board_header.insert(0, "##")

        board_values = list(board_details.values())
        board_values.insert(0, "##")

        task_list.append(["##", "Board Details"])

        task_list.append(board_header)
        task_list.append(board_values)

        task_list.append([""])
        task_list.append(["##", "Task Details"])

        row_count = 1

        for task in board_tasks:

            for field in rm_fields:
                task.pop(field, None)

            if row_count == 1:
                header = list(task.keys())
                header.insert(0, "Sr. No.")
                task_list.append(header)

            row = list(task.values())
            row.insert(0, str(row_count))
            task_list.append(row)
            row_count += 1
        
        file_prefix = f"TeamBoard_{board_name}"
        filename, export_filepath = get_export_filepath(
            subpath="BoardExports",
            file_prefix=file_prefix,
            file_ext="csv"
            )

        with open(export_filepath, 'w', newline='') as data_file:
            csv_writer = csv.writer(data_file)
            csv_writer.writerows(task_list)

        return filename, export_filepath
    
    except Exception as excp:
        return None, None



def export_request(request = None, response = None, http_status = None, subpath = "", file_prefix="")->tuple:
    """Exports the request body to the AppData Dir"""
    try:

        data = (f"Request: \n{json.dumps(request.data, indent=3)}\n\n"
                f"Http Response Status: {http_status}\n\n"
                f"Response: \n{json.dumps(response, indent=3)}"
                )

        filename, export_filepath = get_export_filepath(
                subpath=subpath,
                file_prefix=file_prefix,
                file_ext="txt"
                )
        
        with open(export_filepath, 'w') as fp:
            fp.write(str(data))

        return filename, export_filepath
    except Exception as excp:
        return None, None


# Decorator to handle Response exceptions
def drf_resp_excp_handler(func):
    """Input: Request Handler"""
    def wrapper(*args,**kwargs):
        msg = {"message": " The request could not be fulfilled"}

        try:
            response_data = func(*args, **kwargs)
            return response_data
        except Exception as excp:
            msg["error"] = str(excp)
            response_data = Response(msg, status=500)
            return response_data
    
    return wrapper



