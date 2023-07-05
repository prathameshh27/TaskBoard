from apps.api.versions.v1.viewsets.user_viewset import UserViewSet
from rest_framework.decorators import api_view
from apps.lib.utils.functions import export_request

user = UserViewSet()

@api_view(['GET'])
def index(request):
    response = user.index(request)
    
    filename, filepath = export_request(
            request=request,
            response=response.data,
            http_status=(response.status_code, response.status_text),
            subpath= "User",
            file_prefix="index"
            )

    return response

@api_view(['POST'])
def create_user(request: object) -> object:
    response = user.create_user(request)
    
    filename, filepath = export_request(
            request=request,
            response=response.data,
            http_status=(response.status_code, response.status_text),
            subpath= "User",
            file_prefix="create_user"
            )

    return response

@api_view(['GET'])
def list_users(request: object) -> object:
    response = user.list_users(request)
    
    filename, filepath = export_request(
            request=request,
            response=response.data,
            http_status=(response.status_code, response.status_text),
            subpath= "User",
            file_prefix="list_users"
            )

    return response

@api_view(['GET'])
def describe_user(request: object) -> object:
    response = user.describe_user(request)
    
    filename, filepath = export_request(
            request=request,
            response=response.data,
            http_status=(response.status_code, response.status_text),
            subpath= "User",
            file_prefix="describe_user"
            )

    return response

@api_view(['PATCH'])
def update_user(request: object) -> object:
    response = user.update_user(request)
    
    filename, filepath = export_request(
            request=request,
            response=response.data,
            http_status=(response.status_code, response.status_text),
            subpath= "User",
            file_prefix="update_user"
            )

    return response

@api_view(['GET'])
def get_user_teams(request: object) -> object:
    response = user.get_user_teams(request)
    
    filename, filepath = export_request(
            request=request,
            response=response.data,
            http_status=(response.status_code, response.status_text),
            subpath= "User",
            file_prefix="get_user_teams"
            )

    return response
