from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    """API endpoint for user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User registered successfully',
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message': 'Registration failed',
                'errors': form.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    """API endpoint for user login"""
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Login successful',
                    'user': UserSerializer(user).data,
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Invalid credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'message': 'Username and password are required'
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_api(request):
    """API endpoint for user profile"""
    return Response({
        'user': UserSerializer(request.user).data
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_api(request):
    """API endpoint for user logout"""
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                'message': 'Logout successful'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'Refresh token is required'
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'message': 'Invalid token'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def products_api(request):
    """Products API view"""
    from main.models import Product
    from .serializers import ProductSerializer
    
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    
    return Response({
        'products': serializer.data,
        'count': products.count(),
        'message': 'Products retrieved successfully'
    })
