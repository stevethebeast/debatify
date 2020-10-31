from rest_framework import serializers

from .models import Hero, yourMom, Contact, Debate, Argument, Counter_argument, Debate_vote, Argument_vote,\
Counter_argument_vote, Voting_right, Usergroup, Usergroup_contact

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class momSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = yourMom
        fields = ('name', 'alias')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('ID', 'NAME', 'EMAIL', 'PASSWORD')

class DebateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debate
        fields = ('ID', 'NAME', 'YES_TITLE', 'NO_TITLE', 'CONTEXT', 'PHOTO_PATH', 'YES_SCORE', 'NO_SCORE', 'CONTACT_ID')

class ArgumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Argument
        fields = ('ID', 'TEXT', 'DEBATE_ID', 'SCORE', 'CONTACT_ID', 'SIDE')

class CounterArgumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counter_argument
        fields = ('ID', 'TEXT', 'ARGUMENT_ID', 'SCORE', 'CONTACT_ID')

class DebateVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debate_vote
        fields = ('ID', 'SIDE', 'DEBATE_ID', 'CONTACT_ID')

class ArgumentVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Argument_vote
        fields = ('ID', 'ARGUMENT_ID', 'SCORE', 'CONTACT_ID')

class CounterArgumentVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counter_argument_vote
        fields = ('ID', 'COUNTER_ARGUMENT_ID', 'SCORE', 'CONTACT_ID')

class VotingRightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voting_right
        fields = ('DEBATE_ID', 'CONTACT_ID')

class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usergroup
        fields = ('ID', 'NAME', 'CONTACT_ID')

class UserGroupContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usergroup_contact
        fields = ('CONTACT_ID', 'USERGROUP_ID')
