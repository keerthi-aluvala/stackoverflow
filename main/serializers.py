from rest_framework import serializers

# Importing Models.
from .models import (
    Question,
    Answer,
    Comment,
    UpVote,
    DownVote,
)

# Defining Serializers For various Models.

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UpVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpVote
        fields = '__all__'

class DownVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownVote
        fields = '__all__'