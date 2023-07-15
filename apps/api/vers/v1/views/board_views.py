from apps.api.vers.v1.viewsets.board_viewset import BoardViewSet
from rest_framework.decorators import api_view
from apps.lib.utils.functions import export_request

board = BoardViewSet()

@api_view(['POST'])
def create_board(request: object) -> object:
    response = board.create_board(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "TeamBoard",
        file_prefix="create_board"
        )

    return response

@api_view(['GET'])
def close_board(request: object) -> object:
    response = board.close_board(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "TeamBoard",
        file_prefix="close_board"
        )

    return response

@api_view(['POST'])
def add_task(request: object) -> object:
    response = board.add_task(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "TeamBoard",
        file_prefix="add_task"
        )

    return response

@api_view(['PATCH'])
def update_task_status(request: object) -> object:
    response = board.update_task_status(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "TeamBoard",
        file_prefix="update_task"
        )

    return response

@api_view(['GET'])
def list_boards(request: object) -> object:
    response = board.list_boards(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "TeamBoard",
        file_prefix="list_boards"
        )

    return response

@api_view(['GET'])
def export_board(request: object) -> object:
    response = board.export_board(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "TeamBoard",
        file_prefix="export_board"
        )

    return response


