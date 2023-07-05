from django.db import models
from django.utils import timezone
from apps.lib.utils.functions import custom_id
from .board import Board
from .team import Team
from .user import CustomUser


class Task(models.Model):

    class Status(models.TextChoices):
        OPEN = "OPEN"
        IN_PROGRESS = "IN_PROGRESS"
        COMPLETE = "COMPLETE"

    class Meta:
        unique_together = 'board_id', 'title'
        ordering = ('team_id', 'board_id', '-user_id', 'creation_time')

    id = models.CharField(primary_key=True, max_length=11, unique=True, editable=False, default=custom_id)
    title = models.CharField(null=False, blank=False, editable=False, max_length=64)
    description = models.CharField(null=True, blank=True, max_length=128)
    team_id = models.ForeignKey(Team, related_name="team_tasks", null=True, blank=True, on_delete=models.DO_NOTHING)
    board_id = models.ForeignKey(Board, related_name="board_tasks", null=False, blank=False, default="0000", on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(CustomUser, related_name="user_tasks", null=False, blank=False, default="0000", on_delete=models.DO_NOTHING)
    creation_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.OPEN)
    end_time = models.DateTimeField(null=True, blank=True)

    # returns name and id both for debugging purpose 
    def __str__(self) -> str:
        return "{} ({})".format(self.title, self.id)

    def get_id(self) -> str:
        """Get Task id"""
        return self.id
    
    def get_user(self) -> object:
        """get user object"""
        return self.user_id
    
    def get_board(self) -> object:
        """get board object"""
        return self.board_id
    
    def set_status(self, status:Status) -> bool:
        """Set Task status. status in lower case allowed"""
        try:
            status = status.upper()
            if status in Task.Status:
                self.status = status
                if self.status == self.Status.COMPLETE:
                    self.end_time = timezone.now()
                self.save()
                is_success = True
            else:
                is_success = False
        except Exception as excp:
            is_success = False
        return is_success
    
    @classmethod
    def list_tasks(cls) -> object:
        """List all Tasks"""
        return cls.objects.all()
    
    @classmethod
    def get_task(cls, id:str) -> object:
        """Get task by id"""
        try:
            task = cls.objects.get(id=id)
        except Exception as excp:
            task = None
        return task
    
    @classmethod
    def get_board_task(cls, board_id:str) -> object:
        """Get all task by board id"""
        try:
            tasks = cls.objects.filter(board_id=board_id)
        except Exception as excp:
            tasks = None
        return tasks
    