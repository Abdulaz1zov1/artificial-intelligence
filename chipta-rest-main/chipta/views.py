from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from .models import Yonalish, Bekat, Poyezd, Vagon, Chipta
from .serializers import (YonalishSerializer, 
                          BekatSerializer, PoyezdSerializer,
                          VagonSerializer, ChiptaSerializer)
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import datetime, timedelta


class BekatViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Bekat.objects.all()
    serializer_class = BekatSerializer


class PoyezdViewSet(viewsets.GenericViewSet):
    queryset = Poyezd.objects.all()
    serializer_class = PoyezdSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    inputs = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'yonalish_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='route id'),
        },
        required=['yonalish_id']
    )

    @swagger_auto_schema(request_body=inputs)
    @action(detail=False, methods=['post'])
    def poyezd(self, request):
        """ for filtering trains by route id """

        yonalish_id = request.data['yonalish_id']
        poyezd = Poyezd.objects.get(
            yonalish__id=yonalish_id
        )
        
        data = self.get_serializer(poyezd).data
        vagonlar = VagonSerializer(poyezd.vagonlar, many=True).data
        
        for vagon in vagonlar:
            joylar = Chipta.objects.filter(yonalish__id=yonalish_id, vagon__id=vagon['id'])
            sotilgan_joylar = [joy.joy_raqami for joy in joylar]
            vagon['sotil_joylar_raqami'] = sotilgan_joylar
            del vagon['poyezd']
    
        data['vagonlar'] = vagonlar

        return Response(data)


class ChiptaViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Chipta.objects.all()
    serializer_class = ChiptaSerializer
    permission_classes = [permissions.IsAuthenticated]

    inputs = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'joy_raqami': openapi.Schema(type=openapi.TYPE_INTEGER ),
            'yonalish': openapi.Schema(type=openapi.TYPE_INTEGER ),
            'vagon': openapi.Schema(type=openapi.TYPE_INTEGER )
        },
        required=['joy_raqami', 'yonalish', 'vagon']
    )

    @swagger_auto_schema(operation_description='chipta qo\'shish',
                         request_body=inputs)


    def create(self, request, *args, **kwargs):
        
        result = self.queryset.filter(
            yonalish=request.data['yonalish'],
            vagon=request.data['vagon'],
            joy_raqami=request.data['joy_raqami'],
        )

        if result.count()!=0:
            return Response({"Error": "This ticket has been sold"},
                            status=status.HTTP_400_BAD_REQUEST)
    
        request.data['mijoz'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    @action(detail=False, methods=['get'])
    def my_ticket(self, request):
        """ for filtering ticket by time and routes"""
        
        chipta = Chipta.objects.filter(
            mijoz=request.user
        )
        
        serializer = self.get_serializer(chipta, many=True)
        return Response(serializer.data)


class YonalishViewSet(viewsets.GenericViewSet):
    queryset = Yonalish.objects.all()
    serializer_class = YonalishSerializer
    
    
    inputs = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'qayerdan': openapi.Schema(type=openapi.TYPE_STRING, description='qayerdan ketish haqida ma\'lumot'),
            'qayerga': openapi.Schema(type=openapi.TYPE_STRING, description='qayerga ketish haqida ma\'lumot'),
            'qachon': openapi.Schema(type=openapi.TYPE_STRING, format="date-time", description='qachon ketish haqida ma\'lumot')
        },
        required=['qayerdan', 'qayerga', 'qachon']

    )


    @swagger_auto_schema(operation_description='Chiptalarni yonalish va vaqt bo\'yicha izlab topish',
                         request_body=inputs)
    @action(detail=False, methods=['post'])
    def find_tickets(self, request):
        """ for filtering ticket by time and routes"""

        qayerdan = request.data['qayerdan']
        qayerga = request.data['qayerga']
        qachon = request.data['qachon']

        yonalish = Yonalish.objects.filter(
            qayerdan=qayerdan, qayerga=qayerga,
            jonash_vaqti__date = qachon
        )
        serializer = self.get_serializer(yonalish, many=True)
        return Response(serializer.data)
