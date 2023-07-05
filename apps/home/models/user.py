from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.lib.utils.functions import custom_id

class CustomUser(AbstractUser):
    id = models.CharField(primary_key=True, unique=True, editable=False, default=custom_id, max_length=11)
    display_name = models.CharField(null=False, max_length=64)

    # returns name and id both for debugging purpose 
    def __str__(self) -> str:
        return "{} ({})".format(self.username, self.id)

    def get_id(self) -> str:
        """Get user ID"""
        return self.id
    
    def get_managed_teams(self) -> object:
        """get all teams where the current user is an Admin"""
        return self.managed_teams.all()
    
    def get_teams(self) -> object:
        """Return all Teams the current user belong to"""
        return self.teams.all()
    
    @classmethod
    def list_users(cls) -> object:
        """List all users"""
        return cls.objects.all()
    
    @classmethod
    def get_user(cls, id:str) -> object:
        """Get specific user"""
        try:
            user = cls.objects.get(id=id)
        except Exception as excp:
            user = None
        return user
    
    @classmethod
    def get_selected_users(cls, user_ids:str) -> object:
        """Get all users listed in the user_ids list"""
        try:
            user_ids = user_ids if isinstance(user_ids, list) else [user_ids]
            users = cls.objects.filter(pk__in=user_ids)
        except Exception as excp:
            users = None
        return users
    
    @classmethod
    def delete_user(cls, id:str) -> bool:
        """Delete user by ID"""
        try:
            user = cls.objects.filter(id=id)
            user.delete()
            is_success = True
        except Exception as excp:
            is_success = False
        return is_success
    