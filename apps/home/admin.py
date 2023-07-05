from django.contrib import admin

from .models.user import CustomUser
from .models.team import Team
from .models.board import Board
from .models.task import Task
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ['id','username', 'display_name', 'date_joined', 'last_login', 'is_superuser']

class AdminTeam(admin.ModelAdmin):
    list_display = ['id', 'name', 'admin']

class AdminBoard(admin.ModelAdmin):
    list_display = ['id', 'name', 'team_id', 'creation_time']

class AdminTask(admin.ModelAdmin):
    list_display = ['id', 'title', 'team_id', 'board_id', 'user_id', 'creation_time', 'status']

admin.site.register(CustomUser, AdminUser)
admin.site.register(Team, AdminTeam)
admin.site.register(Board, AdminBoard)
admin.site.register(Task, AdminTask)