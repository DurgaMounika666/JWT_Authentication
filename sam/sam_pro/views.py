from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Login
from .serializers import UserSerializer, LoginSerializer

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, authenticated user!"})

# Create your views here.

@api_view(["POST"])
def Create(request):
    if request.method == "POST":
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Created successfully"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(["GET"])
def All(request):
    if request.user.is_authenticated:
        print("user",request.user)
        user = Login.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    else :
        return Response({"status": "User_Unauthorized"})

@api_view(["PUT"])
def Update(request,id):
    if request.user.is_authenticated:
        user = Login.objects.get(id=id)
        if request.method == "PUT":
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                # return Response(serializer.data)
                return Response({"status":"Updated Successfully"}, status = status.HTTP_200_OK)
            return Response({"status":"Incorrect details"}, status = status.HTTP_400_BAD_REQUEST )
    else:
        return Response({"status": "User_Unauthorized"})

@api_view(["DELETE"])
def Delete(request,id):
    if request.user.is_authenticated:
        user = Login.objects.get(id=id)
        user.delete()
        return Response("User Deleted Successfully")
    else:
        return Response({"status": "User_Unauthorized"})

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    Logout API to blacklist a refresh token.
    """
    try:
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=400)

        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"message": "Logout successful"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

# @api_view(["POST"])
# def UserLogin(request):
#     if request.method == 'POST':
#         serializer = LoginSerializer(Login,data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get('email')
#          @api_view(['POST'])
# def logout_view(request):
#         logout(request)
#         return Response({"message": "Successfully_logged_out."}, status=status.HTTP_200_OK)   password = serializer.validated_data.get('password')
#
#             print("email:",email)
#             print("Password:",password)
#
#             user = authenticate(email=email,password=password)
#             print('user',user)
#
#             print(request)
#             print(request.user)
#
#             if user is not None:
#                 login(request, user)
#                 # user_id = User.objects.get(username=request.user)
#                 return Response({"status": "user_validated"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"status": "unauthorized_user"}, status=status.HTTP_401_UNAUTHORIZED)
#
#
#         return Response({'status': 'Invalid_Credentials'}, status=status.HTTP_400_BAD_REQUEST)
#
#

# @api_view(['POST'])
# def login_view(request):
#     if request.method == 'POST':
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data.get('username')
#             password = serializer.validated_data.get('password')
#
#             print("Username:",username)
#             print("Password:",password)
#
#             user = authenticate(username=username,password=password)
#             print('user',user)
#
#             print(request)
#             print(request.user)
#
#             if user is not None:
#                 login(request, user)
#                 # user_id = User.objects.get(username=request.user)
#                 return Response({"status": "user_validated"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"status": "unauthorized_user"}, status=status.HTTP_401_UNAUTHORIZED)
#
#
#         return Response({'status': 'Invalid_Credentials'}, status=status.HTTP_400_BAD_REQUEST)




from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        # Debugging
        print("Username:", username)
        print("Password:", password)

        Login = authenticate(username=username, password=password)  # Checks User model
        print('Authenticated User:', Login)

        if Login is not None:
            login(request, Login)  # Log the user in (session-based)
            return Response({"status": "user_validated"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "unauthorized_user"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'status': 'Invalid_Credentials'}, status=status.HTTP_400_BAD_REQUEST)

