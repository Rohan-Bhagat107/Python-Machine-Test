from rest_framework import serializers
from .models import User, Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        
class CreateProjectSerializer(serializers.ModelSerializer):
    users = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )  

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        users = validated_data.pop('users')
        project = Project.objects.create(**validated_data)
        project.users.set(users)
        return project
