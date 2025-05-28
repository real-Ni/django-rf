from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status': 200, 'payload': serializer.data})

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RegisterUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors})
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user = user)
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token_obj)})

class StudentAPI(APIView):
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({'status': 200, 'payload': serializer.data})
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data})
    
    def put(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj, data = request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
    
        except Exception as e:
            print(e)
            return Response({'status': 403})
    
    def patch(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj, data = request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
    
        except Exception as e:
            print(e)
            return Response({'status': 403})
        
    def delete(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            student_obj.delete()
            return Response({'status': 200, 'message': 'deleted.'})
        except Exception as e:
            print(e)
            return Response({'status': 403})

# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)
#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
    # serializer = StudentSerializer(data = request.data)
    # if not serializer.is_valid():
    #     print(serializer.errors)
    #     return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
    # serializer.save()
    # return Response({'status': 200, 'payload': serializer.data})

# @api_view(['PUT'])
# def update_student(request, id):
    # try:
    #     student_obj = Student.objects.get(id = id)
    #     serializer = StudentSerializer(student_obj, data = request.data)
    #     if not serializer.is_valid():
    #         print(serializer.errors)
    #         return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
    #     serializer.save()
    #     return Response({'status': 200, 'payload': serializer.data})
    
    # except Exception as e:
    #     print(e)
    #     return Response({'status': 403})
    
# @api_view(['PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializer(student_obj, data = request.data, partial=True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data})
    
#     except Exception as e:
#         print(e)
#         return Response({'status': 403})
    
# @api_view(['DELETE'])
# def delete_student(request, id):
    # try:
    #     student_obj = Student.objects.get(id = id)
    #     student_obj.delete()
    #     return Response({'status': 200, 'message': 'deleted.'})
    # except Exception as e:
    #     print(e)
    #     return Response({'status': 403})