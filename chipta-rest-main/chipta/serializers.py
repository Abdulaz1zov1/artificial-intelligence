from rest_framework.serializers import ModelSerializer
from .models import Yonalish, Bekat, Poyezd, Vagon, Chipta


class BekatSerializer(ModelSerializer):
    class Meta:
        model = Bekat
        fields = "__all__"


class PoyezdSerializer(ModelSerializer):
    class Meta:
        model = Poyezd
        fields = "__all__"


class VagonSerializer(ModelSerializer):
    class Meta:
        model = Vagon
        fields = "__all__"


    def to_representation(self, obj):
        response = super().to_representation(obj)
        response['poyezd'] = obj.poyezd.nomi

        return response


class YonalishSerializer(ModelSerializer):
    
    class Meta:
        model = Yonalish
        fields = "__all__"

        
    def to_representation(self, obj):
        response = super().to_representation(obj)
        response['poyezd'] = obj.poyezd.nomi
        response['qayerdan'] = obj.qayerdan.nomi
        response['qayerga'] = obj.qayerga.nomi
        
        return response


class ChiptaSerializer(ModelSerializer):
    class Meta:
        model = Chipta
        fields = "__all__"


    def to_representation(self, obj):
        response = super().to_representation(obj)
        response['yonalish'] = obj.yonalish.nomi
        response['vagon'] = obj.vagon.raqami
        response['narxi'] = obj.vagon.narxi
        
        return response

    def validate(self, attrs):
        return super().validate(attrs)
