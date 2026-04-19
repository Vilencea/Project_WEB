from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import Register, ChangePass
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class RegisterV(APIView):
    def post(self,request):
        reg_serializer=Register(data=request.data)
        if reg_serializer.is_valid():
            reg_serializer.save()
            return Response({'message':'Вы теперь наш раб!'}, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ChangepassV(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=ChangePass(data=request.data, context={'request':request})
        if serializer.is_valid():
            user=request.user
            user.set_password(serializer.validated_data['новый пароль'])
            user.save()
            return Response({'message':'Пароль изменен'}, status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'Что то пошло не так хз', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginV(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({'token':token.key, 'Наш раб':user.username})

class LogoutVV(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'message':'Вы стали свободным человеком'}, status=status.HTTP_200_OK)
    
