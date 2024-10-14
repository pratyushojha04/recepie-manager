from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecepieSerializer,CreateRecepieSerializer
from .models import Receipe,Ingrdients
class ReceipeAPI(APIView):
    def get(self, request):
        queryset = Receipe.objects.all()
        serializer = RecepieSerializer(queryset, many=True)

        return Response( {
            "status":True,
            "message": "Receipe API is working fine",
            "data" : serializer.data
        })
    
    def post(self, request):
        data = request.data
        print(data)
        serializer = CreateRecepieSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors,
                "data": {}
            })
        serializer.save()

        return Response({
            "status": True,
            "message": "Receipe added successfully",
            "data": {}
        }
        )