from apps.api.versions.v1.viewsets.team_viewset import TeamViewSet
from rest_framework.decorators import api_view
from apps.lib.utils.functions import export_request

team = TeamViewSet()

@api_view(['POST'])
def create_team(request: object) -> object:
    response = team.create_team(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "Team",
        file_prefix="create_team"
        )

    return response

@api_view(['GET'])
def list_teams(request: object) -> object:
    response = team.list_teams()
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "Team",
        file_prefix="list_teams"
        )

    return response

@api_view(['GET'])
def describe_team(request: object) -> object:
    response = team.describe_team(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "Team",
        file_prefix="describe_team"
        )

    return response

@api_view(['PATCH'])
def update_team(request: object) -> object:
    response = team.update_team(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "Team",
        file_prefix="update_team"
        )

    return response

@api_view(['GET'])
def add_users_to_team(request: object) -> object:
    response = team.add_users_to_team(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "Team",
        file_prefix="add_users"
        )

    return response

@api_view(['GET'])
def remove_users_from_team(request: object) -> object:
    response = team.remove_users_from_team(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "Team",
        file_prefix="remove_users"
        )

    return response

@api_view(['GET'])
def list_team_users(request: object) -> object:
    response = team.list_team_users(request)
    
    filename, filepath = export_request(
        request=request,
        response=response.data,
        http_status=(response.status_code, response.status_text),
        subpath= "Team",
        file_prefix="list_users"
        )

    return response

