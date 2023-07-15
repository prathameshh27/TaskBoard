from django.urls import path, include
from .views.user_views import *
from .views.team_views import *
from .views.board_views import *

urlpatterns = [
    path('', index, name='list_users'),
    path('user/create', create_user, name='create_user'),
    path('user/update', update_user, name='update_user'),
    path('user/describe', describe_user, name='describe_user'),
    path('user/list', list_users, name='list_users'),
    path('user/list_teams', get_user_teams, name='get_user_teams'),

    path('team/create', create_team, name='create_team'),
    path('team/update', update_team, name='update_team'),
    path('team/describe', describe_team, name='describe_team'),
    path('team/list', list_teams, name='list_teams'),
    path('team/list_users', list_team_users, name='list_team_users'),
    path('team/add_users', add_users_to_team, name='add_users_to_team'),
    path('team/remove_users', remove_users_from_team, name='remove_users_from_team'),

    path('board/create', create_board, name='create_board'),
    path('board/list', list_boards, name='list_boards'),
    path('board/close', close_board, name='close_board'),
    path('board/add_task', add_task, name='add_task'),
    path('board/update_task_status', update_task_status, name='update_task_status'),
    path('board/export', export_board, name='export_board'),

]