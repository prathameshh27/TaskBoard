from rest_framework import serializers
from apps.home.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    """Model: Task"""
    class Meta:
        """Metadata for the Task Serializer"""
        model = Task
        fields = ('id', 'title', 'description', 'team_id', 'board_id', 'user_id', 'user', 'creation_time', 'end_time', 'status')
        # fields = ('id', 'title', 'description', 'team_id', 'board_id', 'user_id', 'user', 'team', 'board', 'creation_time', 'end_time', 'status')

    title = serializers.CharField(min_length=3, max_length=64, trim_whitespace=True)
    user = serializers.CharField(source='user_id.username', read_only=True)
    # team = serializers.CharField(source='team_id.name', read_only=True)
    # board = serializers.CharField(source='board_id.name', read_only=True)


# class ExpTaskSerializer(serializers.ModelSerializer):
#     """Model: Task"""
#     class Meta:
#         """Metadata for the Task Serializer"""
#         model = Task
#         fields = ('id', 'title', 'description', 'team_id', 'board_id', 'user_id', 'user', 'team_name', 'board_name', 'creation_time', 'end_time', 'status')

#     title = serializers.CharField(min_length=3, max_length=64, trim_whitespace=True)
#     user = serializers.CharField(source='user_id.username', read_only=True)
#     team_name = serializers.CharField(source='team_id.name', read_only=True)
#     board_name = serializers.CharField(source='board_id.name', read_only=True)