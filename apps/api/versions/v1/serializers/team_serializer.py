from rest_framework import serializers
from apps.home.models.team import Team

class TeamSerializer(serializers.ModelSerializer):
    """Model: Team"""
    class Meta:
        """Metadata for the Team Serializer"""
        model = Team
        fields = ('id', 'name', 'description', 'creation_time', 'admin')

    name = serializers.CharField( max_length=64, trim_whitespace=True)

    def update(self, instance, validated_data):
        validated_data.pop('name', None)
        validated_data.pop('creation_time', None)
        instance = super(TeamSerializer,self).update(instance, validated_data)
        return instance
        