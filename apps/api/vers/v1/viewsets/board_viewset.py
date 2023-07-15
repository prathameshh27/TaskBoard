from rest_framework.response import Response
from apps.lib.base.project_board_base import ProjectBoardBase
from ..serializers.team_serializer import Team
from ..serializers.board_serializer import BoardSerializer, ExpBoardSerializer, Board
from ..serializers.task_serializer import TaskSerializer, Task
from copy import deepcopy
from apps.lib.utils.functions import (
    drf_resp_excp_handler, 
    get_validation_errors, 
    export_taskboard
    )


# ToDo: Minimize the use of conditional blocks. 
# Add validations at serializer level instead.

#ToDo: Log the exported files in database.

class BoardViewSet(ProjectBoardBase):

    RESPONSE = {"message": "Something went wrong. The request could not be fulfilled"}
    HTTP_STATUS = 500

    # create a board
    @drf_resp_excp_handler
    def create_board(self, request: object) -> Response:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        post_data = request.data
        team_id = post_data.get("team_id", None)

        team = Team.get_team(team_id)

        if team:
            board_serializer = BoardSerializer(data=post_data, many=False)
            if board_serializer.is_valid():
                board = board_serializer.save()

                board_list = board if isinstance(board, list) else [board]
                board_ids = [board.id for user in board_list]

                response = {
                    "id" : str(board_ids)
                }
                http_status = 201
            else:

                response = {"message" : "Board could not be added"}    
                response["errors"]  = get_validation_errors(board_serializer)
        else:
            response = {"message" : "Team could not be found"}
            http_status = 400
        
        return Response(data=response, status=http_status)

    # ToDo: Apply validations so that only admins can close the board.

    # close a board
    @drf_resp_excp_handler
    def close_board(self, request: object) -> Response:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        req = request.data
        board_id = req.get("id", None)
        if board_id:
            board = Board.get_board(id=board_id)
            if board:
                # ToDo: if tasks are not added then this function will return an empty list. 
                # Hence the board will be closed. Any action required?
                tasks = board.get_pending_tasks()
                if len(tasks) == 0:
                    board.close_board(task_closed = True)
                    response = {"message" : "Board closed"}
                    http_status = 200
                else:
                    response = {"message" : "Please complete the pending tasks before closing the board"}
                    http_status = 200
            else:
                response = {"message" : "Board not found with the supplied id: {}".format(board_id)}
        else:
            response = {"message" : "Please supply a valid 'id' via the request"}

        return Response(data=response, status=http_status)                
    
    # add task to board
    @drf_resp_excp_handler
    def add_task(self, request: object) -> Response:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        post_data = request.data
        board_id = post_data.get("board_id", None)
        user_id = post_data.get("user_id", None)

        if all((board_id, user_id)):
            board = Board.get_board(board_id)
            if board:
                if board.status == Board.Status.OPEN:
                    team = board.get_team()
                    post_data["team_id"] = team.get_id()
                    
                    user = team.get_user(user_id)
                    if user:
                        task_serializer = TaskSerializer(data=post_data, many=False)
                        if task_serializer.is_valid():
                            task = task_serializer.save()

                            task_list = task if isinstance(task, list) else [task]
                            task_ids = [task.id for task in task_list]

                            response = {
                                "id" : str(task_ids)
                            }
                            http_status = 201
                        else:
                            response = {"message": f"The task could not be added."}
                            response["errors"]  = get_validation_errors(task_serializer)
                    else:
                        response = {"message": f"The user doesn't have access to the board {board.name}"}
                else:
                    response = {"message": f"The board is closed. You cannot add a task"}
            else:
                response = {"message": f"The board could not be found"}
        else:
            response = {"message": f"Please supply a valid 'board_id' and 'user_id'"}   

        return Response(data=response, status=http_status)


    # update the status of a task
    @drf_resp_excp_handler
    def update_task_status(self, request: object) -> Response:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        req = request.data
        task_id = req.get("id", None)
        if task_id:
            task = Task.get_task(id=task_id)
            if task:
                status = req.get("status", None)
                is_success = task.set_status(status)
                if is_success:
                    response = {"message": f"Task - {task_id} has been updated successfully"}
                    http_status = 200
                else:
                    response = {"message": f"The status could not be updated"}
            else:
                response = {"message": f"Task not found"}
        else:
            response = {"message": f"Please supply a valid 'id' via the request"}

        return Response(data=response, status=http_status)


    # list all open boards for a team
    @drf_resp_excp_handler
    def list_boards(self, request: object) -> Response:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        req = request.data
        team_id = req.get("id", None)
        if team_id:
            team = Team.get_team(id=team_id)
            if team:
                boards = team.get_boards()
                board_serializer = BoardSerializer(boards, many=True)
                response = board_serializer.data
                http_status = 200
            else:
                response = {"message" : "No team found with the supplied id: {}.".format(team_id) }
                http_status = 200
        else:
            response = {"message" : "Please supply a valid Team 'id' via the request"}
            http_status = 400
        return Response(data=response, status=http_status)

    
    # export board
    @drf_resp_excp_handler
    def export_board(self, request: object) -> Response:
        response = self.RESPONSE
        http_status = self.HTTP_STATUS

        req = request.data
        board_id = req.get("id", None)
        if board_id:
            board = Board.get_board(id=board_id)
            if board:
                board_serializer = ExpBoardSerializer(board, many=False)
                exportable_board = deepcopy(board_serializer.data)
                filename, filepath = export_taskboard(exportable_board)
                response = {
                    "filepath" : filepath,
                    "export_data" : board_serializer.data
                }
                http_status = 200

            else:
                response = {"message" : "Board not found with the supplied id: {}".format(board_id)}
        else:
            response = {"message" : "Please supply a valid 'id' via the request"}
    
        return Response(response, status=http_status)