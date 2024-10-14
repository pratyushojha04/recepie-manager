from rest_framework import serializers
from .models import Receipe, Ingrdients

class InfredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrdients
        fields = '__all__'

class RecepieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = ["receipe_name", "receipe_description", "receipe_image", "receipe_type"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['Ingrdients'] = InfredientsSerializer(instance.receipe_ingrdients.all(), many=True).data
        return data
class CreateRecepieSerializer(serializers.ModelSerializer):
    receipe_slug = serializers.CharField(allow_blank=True,required=False)
    class Meta: 
        model = Receipe
        fields = '__all__'

    def create(self,validated_data):
        print(validated_data)
        return super().create(validated_data)
    
