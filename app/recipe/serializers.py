from rest_framework import serializers
from core.models import Recipe
from django.conf import settings


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        model = Recipe
        fields = RecipeSerializer.Meta.fields + ['description']
