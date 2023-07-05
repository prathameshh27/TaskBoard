from rest_framework import serializers
from .task_serializer import TaskSerializer
from apps.home.models.board import Board

class BoardSerializer(serializers.ModelSerializer):
    """Model: Board"""
    class Meta:
        """Metadata for the Board Serializer"""
        model = Board
        # fields = "__all__"
        fields = ('id', 'name', 'description', 'team_id', 'creation_time')

    name = serializers.CharField(min_length=3, max_length=64, trim_whitespace=True)
        

class ExpBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        # depth = 1
        fields = ('id', 'name', 'description', 'team', 'creation_time', 'end_time', 'status', 'board_tasks')

    board_tasks = TaskSerializer(many=True, read_only=True)
    team = serializers.CharField(source='team_id.name')

