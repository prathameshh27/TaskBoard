from django.db import models
from apps.lib.utils.functions import custom_id
from .user import CustomUser as User

# ToDo: admin on_delete to be handled. Assign some other user from the team or assign super user

class Team(models.Model):
    MAX_USERS = 50

    id = models.CharField(primary_key=True, max_length=11, unique=True, editable=False, default=custom_id)
    name = models.CharField(null=False, blank=False, editable=False, unique=True, max_length=64)
    description = models.CharField(null=True, blank=True, max_length=128)
    creation_time = models.DateTimeField(auto_now=True, editable=False)
    admin = models.ForeignKey(to=User, null=False, related_name="managed_teams", on_delete=models.DO_NOTHING)
    users = models.ManyToManyField(to=User, blank=True, related_name="teams")
    
    # The save method is overridden to add admin to the team.users by default 
    def save(self, *args, **kwargs):
        super(Team, self).save(*args, **kwargs)
        self.add_users([self.admin])

    # returns name and id both for debugging purpose 
    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.id)

    def get_id(self) -> str:
        """Get Team ID"""
        return self.id
    
    def get_users(self) -> object:
        """Get all users that belong to the current Team"""
        return self.users.all()
    
    def get_user(self, user_id:str) -> object:
        """Get a specific user that belogs to a team. 
        If user not found then None would be returned"""
        try:
            user = self.users.get(id=user_id)
        except Exception as excp:
            user = None
        return user
    
    def get_boards(self) -> object:
        """Get all boards that belong to the current team"""
        return self.boards.all()
    
    def add_users(self, users:list) -> bool:
        """Add users to the team. Please pass the users through a list even if it is one"""
        try:
            team_strength = self.users.count()
            if team_strength <= self.MAX_USERS:
                self.users.add(*users)
                return True
            else:
                return False
        except Exception as excp:
            return False

    def remove_users(self, users:list) -> bool:
        """Remove users from the team. Please pass the users through a list even if it is one"""
        try:
            self.users.remove(*users)
            return True
        except Exception as excp:
            return False        
        

    @classmethod
    def list_teams(cls) -> object:
        """List all Teams"""
        return cls.objects.all()
    
    @classmethod
    def get_team(cls, id:str) -> object:
        """Get team by id"""
        try:
            team = cls.objects.get(id=id)
        except Exception as excp:
            team = None
        return team
    
    @classmethod
    def delete_team(cls, id:str) -> bool:
        """delete team by id"""
        try:
            team = cls.objects.filter(id=id)
            team.delete()
            is_success = True
        except Exception as excp:
            is_success = False
        return is_success
    