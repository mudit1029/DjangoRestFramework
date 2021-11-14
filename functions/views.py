from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer
# Create your views here.

@api_view(['GET'])
def showAll(request):
	data = employee.objects.all()
	serializer = employeeSerializer(data, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def showID(request, pk):
	data = employee.objects.get(id=pk)
	serializer = employeeSerializer(data)
	return Response(serializer.data)	

@api_view(['POST'])
def add(request):
	serializer = employeeSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response("Saved Successfully")

@api_view(['GET','PUT'])
def update(request, pk):
	data = employee.objects.get(id=pk)
	if request.method == "GET":
		return Response(employeeSerializer(data).data)		
	serializer = employeeSerializer(data , data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)

@api_view(['GET','DELETE'])
def delete(request, pk):
	data = employee.objects.get(id=pk)
	serializer = employeeSerializer(data)
	if request.method == 'DELETE':
		data.delete()
		return Response("Successfully Deleted")					
	return Response(serializer.data)				
