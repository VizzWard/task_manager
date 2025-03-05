from rest_framework import serializers
from django.utils import timezone

from .models import TagsUser, Tasks, Comments
from users.models import User

class TagsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsUser
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'description',
            'progress',
            'priority',
            'start_date',
            'end_date',
            'state',
            'created_at',
            'modified_at' ,
            'tag_name'
        ]

    def get_tag_name(self, obj):
        return obj.tag.name if obj.tag else None

# Serializador para obtener las tareas con pocos detalles
class GetTasksSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'progress',
            'priority',
            'tag_name',
            'created_at',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si en el contexto se indica que se deben mostrar todas las tareas, agregar "state"
        if self.context.get('include_state', False):
            self.fields['state'] = serializers.BooleanField()

    def get_tag_name(self, obj):
        return obj.tag.name if obj.tag else None

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'comment', 'created_at']

def last_login(id):
    user = User.objects.filter(id=id).first()
    user.last_login = timezone.now()
    user.save()