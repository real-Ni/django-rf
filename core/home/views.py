from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import *
# Create your views here.

@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status': 200, 'payload': serializer.data})

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)
    return Response({'status': 200, 'payload': serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
    serializer.save()
    return Response({'status': 200, 'payload': serializer.data})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id = id)
        serializer = StudentSerializer(student_obj, data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data})
    
    except Exception as e:
        print(e)
        return Response({'status': 403})
    
@api_view(['PATCH'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id = id)
        serializer = StudentSerializer(student_obj, data = request.data, partial=True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data})
    
    except Exception as e:
        print(e)
        return Response({'status': 403})
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id = id)
        student_obj.delete()
        return Response({'status': 200, 'message': 'deleted.'})
    except Exception as e:
        print(e)
        return Response({'status': 403})