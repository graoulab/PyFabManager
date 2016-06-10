# coding: utf-8 
from rest_framework import serializers
from ..models import Machine
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from rest_framework.decorators import api_view, api_view
from rest_framework.response import Response


class ListMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'Titre', 'Image')
class InfoMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'Titre', 'Image', 'Descritpion','Cout','CoutAdh','Projet','fichier')

@api_view(['GET'])
def GetListMachine(request):
    if request.method == 'GET':
        page = 1
        if request.GET.get('page') and request.GET.get('page').isdigit():
            page = request.GET.get('page')
        nbelement = 10
        data = list(Machine.objects.all())
        paginator = Paginator(data, nbelement)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        serializer = ListMachineSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetMachineInfo(request):
    if request.method == 'GET':
        MachineId = 0
        if request.GET.get('MachineId') and request.GET.get('MachineId').isdigit():
            MachineId = request.GET.get('MachineId')
        serializer = InfoMachineSerializer(Machine.objects.filter(id=MachineId), many=True)
        return Response(serializer.data)