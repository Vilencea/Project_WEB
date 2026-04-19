from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import checkoutSerial
from .models import order, orderItem
from menu.models import Product

class CheckV(APIView):
    permission_classes=[IsAuthenticated]
    def post (self,request):
        serializer=checkoutSerial(data=request.data)
        if serializer.is_valid():
            order= order.objects.create(user=request.user)
            items=serializer.validated_data['items']
            for item in items:
                Product_id=item['product_id']
                quan=item['quantity']
                product=Product.objects.get(id=Product_id)
                orderItem.objects.create(order=order,product=product,quantity=quan)
            return Response({'message':'Заказ принят','номер заказа':order.id}, status=status.HTTP_201_CREATED)
        return Response({'message':'Заказ не оформлен'}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class historyV(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        orders=order.objects.complete().filter(user=request.user)
        data=[{"id":order.id,"Создано в":order.create,"Выполнен":order.complete} for order in orders]
        return Response(data,status=status.HTTP_200_OK)

