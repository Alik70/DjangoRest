from rest_framework import serializers
from games.models import Game, Player, PlayerScore, GameCategory
from games.views import *
from rest_framework import serializers
from games.models import GameCategory
from games.models import Game
from games.models import Player
from games.models import PlayerScore


# class GameSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     release_date = serializers.DateTimeField()
#     game_category = serializers.CharField(max_length=200)
#     played = serializers.BooleanField(required=False)
#
#     def create(self, validated_data):
#         return Game.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.release_date = validated_data.get('release_date', instance.release_date)
#         instance.game_category = validated_data.get('game_category', instance.game_category)
#         instance.played = validated_data.get('played', instance.played)
#         instance.save()
#         return instance

# we user model serializers to eliminate duplicate code, and the create and update is
# the generic behavior of the modelserializers


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    # game's urls related to this category(has fkeys to this)

    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail')

    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    # category name for each game
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'game_category',
            'name',
            'release_date',
            'played')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    # just name of the game.

    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'game',
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    # scores of player the whole score serializer here.
    scores = ScoreSerializer(many=True, read_only=True)
    # just the gender choices
    gender = serializers.ChoiceField(
        choices=Player.GENDER_CHOICES)
    # description of its gender
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'scores',
        )


class PlayerScoreSerializer(serializers.ModelSerializer):
    # just like above again slug fields are just for urls.
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game',
        )
