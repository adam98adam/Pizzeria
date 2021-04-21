from django.shortcuts import render
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import AccountSerializer
from .models import Account
import json


class AccountView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(APIView):
    lookup_url_kwarg = "login"

    def post(self, request, format=None):

        login = request.data.get("login")
        password = request.data.get("password")
        if login == None:
            return Response({"Bad Request": "Can't find login"}, status=status.HTTP_400_BAD_REQUEST)

        account = Account.objects.filter(login=login)
        if len(account) > 0:
            account_password = account.values_list("password", flat=True)[0]
            if account_password == password:
                data = serializers.serialize('json', account)
                return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
            error = {
                "error": "Invalid password",
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        error = {
            "error": "Invalid login",
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
