from rest_framework import serializers
from core.models import Recipe, Tag
from django.conf import settings


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes',
                  'price', 'link', 'description', 'tags']
        read_only_fields = ['id']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        user = self.context['request'].user
        recipe = Recipe.objects.create(**validated_data)

        for tag in tags_data:
            tag_name = tag.get('name') if isinstance(tag, dict) else str(tag)
            tag_obj, _ = Tag.objects.get_or_create(user=user, name=tag_name)
            recipe.tags.add(tag_obj)

        return recipe


class RecipeDatailSerializer(RecipeSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        model = Recipe
        fields = RecipeSerializer.Meta.fields + ['description']
