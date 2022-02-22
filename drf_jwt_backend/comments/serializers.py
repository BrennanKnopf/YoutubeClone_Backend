from cgitb import text
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user','video_id', 'text', 'likes', 'dislikes']