from rest_framework import serializers
from apps.home.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    """Model: Task"""
    class Meta:
        """Metadata for the Task Serializer"""
        model = Task
        fields = ('id', 'title', 'description', 'team', 'board', 'user', 'creation_time', 'end_time', 'status')

    title = serializers.CharField(min_length=3, max_length=64, trim_whitespace=True)
    team = serializers.CharField(source='team_id.name')
    user = serializers.CharField(source='user_id.username')
    board = serializers.CharField(source='board_id.name')

