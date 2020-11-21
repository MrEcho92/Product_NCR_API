from django.shortcuts import render
from .models import ProductNCR
from .serializers import ProductNCRSerializer
from rest_framework import viewsets

# Create your views here.
class ProductNCRViewSet(viewsets.ModelViewSet):
    '''
    ModelViewSet
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    '''
    queryset = ProductNCR.objects.all()
    serializer_class = ProductNCRSerializer
