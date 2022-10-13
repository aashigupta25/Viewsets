from django.shortcuts import render
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class PersonViewSet(viewsets.ViewSet):
    def List(self, request):
        # print("*****List*****")
        # print("Basename:", self.basename)
        # print("Action:", self.action)
        # print("Details:", self.detail)
        # print("Suffix:", self.suffix)
        # print("Namee:", self.name)
        # print("Description:", self.description)

        per = Person.objects.all()
        serializer = PersonSerializer(per, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        id = pk
        if id is not None:
            per = Person.objects.get(id=id)
            serializer = PersonSerializer(per)
        return Response(serializer.data)

    def create(self, request):
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        per = Person.objects.get(pk=id)
        serializer = PersonSerializer(per, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        per = Person.objects.get(pk = id)
        serializer = PersonSerializer(per, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        id = pk
        per = Person.objects.get(pk = id)
        per.delete()
        return Response({'msg':'Data Deleted'})
        

