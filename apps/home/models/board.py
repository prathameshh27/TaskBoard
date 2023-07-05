from django.db import models
from apps.lib.utils.functions import custom_id
from .team import Team
from django.db.models import Q
from django.utils import timezone

# ToDo: If team is deleted then the board status should change to INACTIVE. 
# This will prevent the users from entering tasks.

class Board(models.Model):

    class Status(models.TextChoices):
        OPEN = "OPEN"
        CLOSED = "CLOSED"
        INACTIVE = "INACTIVE"

    class Meta:
        unique_together = 'team_id', 'name'
        ordering = ('team_id', )

    id = models.CharField(primary_key=True, max_length=11, unique=True, editable=False, default=custom_id)
    name = models.CharField(null=False, blank=False, editable=False, max_length=64)
    description = models.CharField(null=True, blank=True, max_length=128)
    team_id = models.ForeignKey(Team, related_name="boards", on_delete=models.DO_NOTHING)
    creation_time = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.OPEN)
    end_time = models.DateTimeField(default="2000-01-01 00:00:00.000000+00:00")

    # returns name and id both for debugging purpose
    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.id)

    def get_id(self) -> str:
        """Get Board id"""
        return self.id
    
    def get_team(self) -> object:
        """Get team object"""
        return self.team_id
    
    def get_tasks(self) -> object:
        """get all tasks -> queryset"""
        return self.board_tasks.all()
    
    def get_pending_tasks(self):
        """Get all pending tasks from the current board.
        Returns all tasks where status is not 'COMPLETE'"""
        tasks = self.get_tasks()
        return tasks.filter(~Q(status="COMPLETE"))
    
    def close_board(self, task_closed:bool) -> bool:
        """Close current board. Pass true for confirmation"""
        if task_closed:
            self.status = self.Status.CLOSED
            self.end_time = timezone.now()
            staus = True
            self.save()
        else:
            staus = False
        return staus
    
    @classmethod
    def list_boards(cls) -> object:
        """List all boards"""
        return cls.objects.all()
    
    @classmethod
    def get_board(cls, id:str) -> object:
        """get board by ID"""
        try:
            board = cls.objects.get(id=id)
        except Exception as excp:
            board = None
        return board
    
    
    