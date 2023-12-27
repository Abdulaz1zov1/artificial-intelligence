
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']

    def to_representation(self, instance):
        return {
            "idsi": instance.id, 
            "name": instance.name,
            "dates": {
                "created_at": instance.created_at, 
                "updated_at": instance.updated_at, 
            },
            "news-list":[{
                "id": i.id,
                "name": i.name,
                "text": i.matn,
                "created_at": i.created_at,
                "updated_at": i.updated_at,
            } for i in instance.news.all()]
        }