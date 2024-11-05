from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from authentications.serializers import UserLoginSerializer, UserSerializer
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly



class UserRegistrationView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User created successfully!',
                'user': {
                    'username': user.username,
                    'email': user.email
                },
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            })
        return Response(serializer.errors)
    




class UserLoginView(APIView):
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                login(request,user)
                return Response({
                     'message': 'User loggedin successfully!',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
        return Response({"detail": "Invalid credentials."})




class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token is None:
            return Response({"detail": "Refresh token required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
          
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)

            return Response({"detail": "Successfully logged out."})
        except Exception as e:
            return Response({"detail": str(e)})

