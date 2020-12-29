from rest_framework import serializers

from .models import Debate, Argument, Counter_argument, Debate_vote, Argument_vote,\
Counter_argument_vote, Category, User, ChatComment

class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = ('ID', 'NAME', 'YES_TITLE', 'NO_TITLE', 'CONTEXT', 'PHOTO_PATH', 'IS_PUBLIC', 'CREATOR_ID', 'CATEGORY_ID', 'CREATED_AT')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('ID', 'NAME', 'COLOR')

class ArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument
        fields = ('ID', 'TITLE', 'TEXT', 'DEBATE_ID', 'SCORE', 'CONTACT_ID', 'SIDE', 'CREATED_AT')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'email', 'mail_confirmed')

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

class ChatCommentListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        ChatComments = [ChatComment(**item) for item in validated_data]
        return ChatComment.objects.bulk_create(ChatComments)

class ChatCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatComment
        fields = ('ID', 'CONTACT_ID', 'DATE', 'TEXT', 'DEBATE_ID')
        list_serializer_class = ChatCommentListSerializer
