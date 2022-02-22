from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view,permission_classes
from .models import Comment
from .serializers import CommentSerializer
from django.contrib.auth.models import User
from django.http import Http404


# Create your views here.


class CommentList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def post_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)