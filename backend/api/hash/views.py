from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data
from .models import Hashes
from .serializers import HashesSerializer

# Create your views here.

class ListCreateHashesView(generics.ListCreateAPIView):
    """
    GET hashes/
    POST hashes/
    """
    queryset = Hashes.objects.all()
    serializer_class = HashesSerializer

    #@validate_request_data
    def post(self, request, *args, **kwargs):
        a_hash = Hashes.objects.create(
            hashValue=request.data["hashValue"],
        )
        #should default set to one for above
        return Response(
            data= HashesSerializer(a_hash).data,
            status=status.HTTP_201_CREATED
        )

    
class HashesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET hashes/:hash/
    PUT hashes/:hash/
    DELETE hashes/:hash/
    """
    queryset = Hashes.objects.all()
    serializer_class = HashesSerializer

    def get(self, request, *args, **kwargs):

        #if the record does not exist it should be added to the db
        try:
            a_hash = self.queryset.get(pk=kwargs["pk"])
            return Response(HashesSerializer(a_hash).data)
        except Hashes.DoesNotExist:
            return Response(
                data={
                    "message": "Hash with value: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    #@validate_request_data

    #change this so that when called the frequency will be increased by 1
    #must be done
    def put(self, request, *args, **kwargs):
        try:
            a_hash = self.queryset.get(pk=kwargs["pk"])
            serializer = HashesSerializer()
            updated_hash = serializer.update(a_hash, request.data)
            return Response(HashesSerializer(updated_hash).data)
        except Hashes.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_hash = self.queryset.get(pk=kwargs["pk"])
            a_hash.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Hashes.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
            