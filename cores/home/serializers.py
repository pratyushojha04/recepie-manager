from rest_framework import serializers
from .models import Receipe, Ingrdients
from django.template.defaultfilters import slugify
import uuid

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
        data['Ingrdients'] = InfredientsSerializer(instance.receipe_ingredents.all(), many=True).data
        return data
    





class CreateRecepieSerializer(serializers.ModelSerializer):
    receipe_slug = serializers.CharField(allow_blank=True,required=False)
    receipe_ingredents = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta: 
        model = Receipe
        fields = '__all__'

    def create(self,validated_data):
        print(validated_data)
        receipe_slug = slugify(validated_data['receipe_name'])
        if Receipe.objects.filter(receipe_slug=receipe_slug).exists():
            receipe_slug = f"{receipe_slug}_{str(uuid.uuid4()).split('-')[0]}"


        recepie = Receipe.objects.create(
            receipe_name=validated_data['receipe_name'],
            receipe_description=validated_data['receipe_description'],
            #receipe_image=validated_data['receipe_image'],
            receipe_slug = receipe_slug,
            receipe_type=validated_data['receipe_type'],
        )
        for ri in validated_data.get("receipe_ingredents"):
            Ingrdients.objects.create(
                reciepe = recepie,
                ingredient_name=ri,
            )





        return recepie
    
