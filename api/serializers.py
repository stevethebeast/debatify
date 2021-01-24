from rest_framework import serializers

from .models import Debate, Argument, Counter_argument, Debate_vote, Argument_vote,\
Counter_argument_vote, User, ChatComment, RecentChatComments

class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = '__all__'

class ArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument
        fields = '__all__'
        read_only_fields = ['SCORE']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CounterArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter_argument
        fields = '__all__'
        read_only_fields = ['SCORE']

class DebateVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate_vote
        fields = '__all__'

class ArgumentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument_vote
        fields = '__all__'

class CounterArgumentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter_argument_vote
        fields = '__all__'

class ChatCommentListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        ChatComments = [ChatComment(**item) for item in validated_data]
        return ChatComment.objects.bulk_create(ChatComments)

class ChatCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatComment
        fields = '__all__'
        list_serializer_class = ChatCommentListSerializer

class RecentChatCommentsListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        RecentChatComments = [RecentChatComments(**item) for item in validated_data]
        return ChatComment.objects.bulk_create(RecentChatComments)

class RecentChatCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentChatComments
        fields = '__all__'
        list_serializer_class = RecentChatCommentsListSerializer
