from rest_framework import serializers
from .models import Projet
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projet
        fields = ('id', 'titre', 'Utilisateur', 'Image')

@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        page = 1
        if request.GET.get('page') and request.GET.get('page').isdigit():
            page = request.GET.get('page')
        nbelement = 10
        data = list(Projet.objects.all())
        paginator = Paginator(data, nbelement)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
