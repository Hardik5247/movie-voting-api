from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
