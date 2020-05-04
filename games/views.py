from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse
from games.models import *
from games.permissions import IsOwnerReadOnly
from games.serializers import *


# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# the restframework response class will do the neccessary negotiations
# related to content features and render, receives the data to the right content type

# this decorator sets a csrf cookie not suitable for production
# @csrf_exempt

# @api_view(['POST', 'GET'])
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         # when many is set to true django uses listserializer. for many instances
#         games_serializer = GameSerializer(games, many=True)
#         return Response(games_serializer.data)
#
#     elif request.method == 'POST':
#         # game_data = JSONParser().parse(request)
#         game_serializer = GameSerializer(data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # @csrf_exempt
# @api_view(['GET', 'POST', 'PUT'])
# def game_detail(request, pk):
#     try:
#         game = Game.objects.get(id=pk)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         game_serializer = GameSerializer(game)
#         return Response(game_serializer.data)
#     elif request.method == 'PUT':
#         # game_data = JSONParser().parse(request)
#         game_serializer = GameSerializer(game, data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data)
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         game.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'scores': reverse(PlayerScoreList.name, request=request),
            'users': reverse(UserList.name, request=request),
        })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerReadOnly
    )


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'


class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'
