from rest_framework import serializers
from apps.home.models.user import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """Model: CustomUser"""
    class Meta:
        """Metadata for the User Serializer"""
        model = CustomUser
        fields = ('id', 'name', 'display_name', 'date_joined')
    
    name = serializers.CharField(source="username", min_length=3, max_length=64, trim_whitespace=True) #64
    
    
    def update(self, instance, validated_data):
        validated_data.pop('name', None)
        validated_data.pop('username', None)
        validated_data.pop('date_joined', None)
        instance = super(UserSerializer,self).update(instance, validated_data)
        return instance
    
    def to_representation(self, instance):
        """date_joined renamed to crat"""
        data = super().to_representation(instance)
        data['creation_time'] = data.get('date_joined', None)
        if data['creation_time']:
            del data['date_joined']
        return data
        