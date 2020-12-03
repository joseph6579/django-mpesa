from django.urls import path
from .views import CreateLNMTransaction
from django import urls

urlpatterns = [
    path('store_LNM/', CreateLNMTransaction.as_view(), name="store_LNM"),
]
