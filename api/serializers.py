from rest_framework import serializers

from .models import Debate, Argument, Counter_argument, Debate_vote, Argument_vote,\
Counter_argument_vote

class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = ('ID', 'NAME', 'YES_TITLE', 'NO_TITLE', 'CONTEXT', 'PHOTO_PATH', 'IS_PUBLIC', 'CREATOR_ID', 'CREATED_AT')

class ArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument
        fields = ('ID', 'TITLE', 'TEXT', 'DEBATE_ID', 'SCORE', 'CONTACT_ID', 'SIDE', 'CREATED_AT')

class CounterArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter_argument
        fields = ('ID', 'TITLE', 'TEXT', 'ARGUMENT_ID', 'SCORE', 'CONTACT_ID', 'CREATED_AT')

class DebateVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate_vote
        fields = ('ID', 'SIDE', 'DEBATE_ID', 'CONTACT_ID', 'CREATED_AT')

class ArgumentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument_vote
        fields = ('ID', 'ARGUMENT_ID', 'LIKE', 'CONTACT_ID', 'CREATED_AT')

class CounterArgumentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter_argument_vote
        fields = ('ID', 'COUNTER_ARGUMENT_ID', 'LIKE', 'CONTACT_ID', 'CREATED_AT')

class DebateArgumentsSerializer(serializers.Serializer):
    SIDE = serializers.CharField(max_length=3)
    ID = serializers.IntegerField()
    TITLE = serializers.CharField(max_length=500)
    SCORE = serializers.IntegerField()
    Username = serializers.CharField(max_length=100)

class GetCounterArgumentByArgumentIDSerializer(serializers.Serializer):
    ID = serializers.IntegerField()
    TITLE = serializers.CharField(max_length=200)
    TEXT = serializers.CharField(max_length=600)
    SCORE = serializers.IntegerField()
    Username = serializers.CharField(max_length=60)

class GetTokenUsernameSerializer(serializers.Serializer):
    EMAIL = serializers.CharField(max_length=50)
