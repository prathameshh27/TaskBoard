from rest_framework.response import Response
from apps.lib.base.team_base import TeamBase
from ..serializers.user_serializer import UserSerializer, CustomUser
from ..serializers.team_serializer import TeamSerializer, Team
from apps.lib.utils.functions import (
    drf_resp_excp_handler, 
    get_validation_errors
    )

# ToDo: Minimize the use of conditional blocks. 
# Add validations at serializer level instead.

class TeamViewSet(TeamBase):

    RESPONSE = {"message": "Something went wrong. The request could not be fulfilled"}
    HTTP_STATUS = 500

    # create a team
    @drf_resp_excp_handler
    def create_team(self, request: object) -> object:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        post_data = request.data
        is_list = True if isinstance(post_data, list) else False
        team_serializer = TeamSerializer(data=post_data, many=is_list)

        if team_serializer.is_valid():
            team = team_serializer.save()

            team_list = team if isinstance(team, list) else [team]
            team_ids = [team.id for user in team_list]

            response = {
                "id" : str(team_ids)
            }
            http_status = 201
        else:
            response = {"message" : "Team could not be added"}
            response["errors"]  = get_validation_errors(team_serializer)
        
        return Response(data=response, status=http_status)

    # list all teams
    @drf_resp_excp_handler
    def list_teams(self) -> object:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        teams = Team.list_teams()
        team_serializer = TeamSerializer(teams, many=True)
        response = team_serializer.data
        http_status = 200
        return Response(response, status=http_status)

    # describe team
    @drf_resp_excp_handler
    def describe_team(self, request: object) -> object:

        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        req = request.data
        team_id = req.get("id", None)
        if team_id:
            team = Team.get_team(id=team_id)
            if team:
                team_serializer = TeamSerializer(team, many=False)
                response = team_serializer.data
                http_status = 200
            else:
                response = {"message" : "No team found with the supplied id: {}.".format(team_id) }
                http_status = 200
        else:
            response = {"message" : "Please supply a valid 'id' via the request"}
            http_status = 400
        return Response(response, status=http_status)

    # update team
    @drf_resp_excp_handler
    def update_team(self, request: object) -> object:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        post_data = request.data
        team_id = post_data.get("id", None)
        team_data = post_data.get("team", None)

        if all((team_id, team_data)):
            team = Team.get_team(team_id)
            if team:
                team_serializer = TeamSerializer(instance=team, data=team_data)
                if team_serializer.is_valid():
                    team_serializer.save()
                    response = team_serializer.data
                else:
                    response = {"message" : "Team could not be updated"}
                    response["errors"]  = get_validation_errors(team_serializer)
            else:
                request = {"message" : "Team not found"}
        else:
            request = {"message" : "Please supply a valid 'id' and 'team' data via the request"}
        
        return Response(data=response, status=http_status)

    # add users to team
    @drf_resp_excp_handler
    def add_users_to_team(self, request: object):
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        # ToDo: Minimize the use of conditional blocks.
        req = request.data
        team_id = req.get("id", None)
        if team_id:
            team = Team.get_team(id=team_id)
            if team:
                user_ids = req.get("users", [])
                users = CustomUser.get_selected_users(user_ids=user_ids)
                if users:
                    is_success = team.add_users(users)
                    if is_success:
                        response = {"message" : "Users added to the team".format(team_id) }
                        http_status = 200
                    else:
                        response = {"message" : "Users could not be added".format(team_id) }
                        http_status = 400
                else:
                    response = {"message" : "Users not found.".format(team_id) }    
                    http_status = 200
            else:
                response = {"message" : "No team found with the supplied id: {}.".format(team_id) }
                http_status = 200
        else:
            response = {"message" : "Please supply a valid 'id' via the request"}
            http_status = 400
        return Response(response, status=http_status)

    # add users to team
    @drf_resp_excp_handler
    def remove_users_from_team(self, request: object):
        response = self.RESPONSE
        http_status = self.HTTP_STATUS


        req = request.data
        team_id = req.get("id", None)
        if team_id:
            team = Team.get_team(id=team_id)
            if team:
                user_ids = req.get("users", [])
                users = CustomUser.get_selected_users(user_ids=user_ids)
                if users:
                    is_success = team.remove_users(users)
                    if is_success:
                        response = {"message" : "Users removed from the team".format(team_id) }
                        http_status = 200
                    else:
                        response = {"message" : "Users could not be removed".format(team_id) }
                        http_status = 400
                else:
                    response = {"message" : "Users not found.".format(team_id) }    
                    http_status = 200
            else:
                response = {"message" : "No team found with the supplied id: {}.".format(team_id) }
                http_status = 200
        else:
            response = {"message" : "Please supply a valid 'id' via the request"}
            http_status = 400
        return Response(response, status=http_status)

    # list users of a team
    @drf_resp_excp_handler
    def list_team_users(self, request: object):
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        req = request.data
        
        team_id = req.get("id", None)
        if team_id:
            team = Team.get_team(team_id)
            if team:
                users = team.get_users()
                user_serializer = UserSerializer(users, many=True)
                response = user_serializer.data
                http_status = 200
            else:
                response = {"message" : "No team found with the supplied id: {}.".format(team_id) }
                http_status = 200
        else:
            response = {"message" : "Please supply a valid 'id' via the request"}
            http_status = 400
        return Response(response, status=http_status)

