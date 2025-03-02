from rest_framework import generics,status,views,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer,LoginSerializer,LogoutSerializer

# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self,request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successful'}, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Logout success'} ,status=status.HTTP_204_NO_CONTENT)

class UserSettingsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        user = request.user
        return Response({
            'notification': user.usersettings.notification,
            'night_mode': user.usersettings.night_mode
        })

    def patch(self,request):
        user = request.user
        user.usersettings.notification = request.data['notification']
        user.usersettings.night_mode = request.data['night_mode']
        user.usersettings.save()
        return Response({
            'success': True,
            'id': user.id,
            'notification': user.usersettings.notification,
            'night_mode': user.usersettings.night_mode
        })