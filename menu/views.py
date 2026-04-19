from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Avg
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, reviews
from .serializers import CategorySerial, ProductSerial, ReviewSerial


@api_view(['GET'])
def categorylist(request):
    categories=Category.objects.all()
    serializers=CategorySerial(categories,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def productlist(request):
    products=Product.objects.all()
    serializers=ProductSerial(products,many=True)
    return Response(serializers.data) 

@api_view(['GET'])
def search(request):
    query=request.queryparams.get('name','')
    if query:
        products=Product.objects.filter(name__icontains=query)
        serializers=ProductSerial(products,many=True)
        return Response(serializers.data)
    return Response({'message':'Введиите имееющий хавчик'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def best(request):
    best_pro=Product.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('avg_rating__gt=4.2')[:3]
    serializers=ProductSerial(best_pro,many=True)
    return Response({"Статус":"Выбор гениев",
                      "Количество": best_pro.count(),
                      "Результаты": serializers.data})

class CategoryV(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerial

class ProductV(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerial

    
