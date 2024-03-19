
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
from .redis import RedisManager
import json


class UserProfileList(APIView):
    def get(self, request):
        redis_manager = RedisManager()
        key = 'profile_data'
        cache = redis_manager.get_redis_cache(key=key)
        if cache:
            json_data = json.loads(cache)
            context = { "message": "success", "isCached": "Yes", "data": json_data }
            return Response(context)
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        json_string = json.dumps(serializer.data)
        redis_manager.set_redis_cache(key=key, value=json_string)
        context = { "message": "success", "isCached": "No", "data": serializer.data }
        return Response(context)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            redis_manager = RedisManager()
            key = 'profile_data'
            redis_manager.delete_redis_cache(key=key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
