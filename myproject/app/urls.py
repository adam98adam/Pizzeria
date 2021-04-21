from django.contrib import admin
from django.urls import path, include
from .views import AccountDetailView, AccountView

urlpatterns = [
    path('account', AccountView.as_view()),
    path('login/', AccountDetailView.as_view()),
]
