from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    members = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "description", "owner", "members"]

    """
    Why this function?
    well, In drf the ModelSerializer automatically uses "PrimaryKeyrelatedfield" for the Many-to-Many fields and Foreign key fields.
    Primarykeyrelatedfield is the default serializer for relationship fields. Its only job is to return the pk ie id of the related field.
    This is for efficiency as send the nested objects need more databse hits.
    There can be other options for this such as :
    Creating a nested serializer
    """

    def get_members(self, obj):
        return [user.email for user in obj.members.all()]


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "description", "owner", "members"]

