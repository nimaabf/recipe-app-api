from rest_framework import serializers
from core.models import Recipe, Tag
from django.conf import settings


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes',
                  'price', 'link', 'description']
        read_only_fields = ['id']


class RecipeDatailSerializer(RecipeSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        model = Recipe
        fields = RecipeSerializer.Meta.fields + ['description']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag,
        fields = ['id', 'name']
        read_only_fields = ['id']
