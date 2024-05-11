from django.shortcuts import render
from .models import GuestBook
from .serializers import GuestBookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from config.permissions import CorrectPassword

class GuestBookListCreate(generics.ListCreateAPIView):
    queryset = GuestBook.objects.all().order_by('-created_at')
    serializer_class = GuestBookSerializer

class GuestBookRetrieveDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = [CorrectPassword]

    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer
    lookup_field = 'id'
