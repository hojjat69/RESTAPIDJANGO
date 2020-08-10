from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers, models, permission
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test API VIEW"""
    serializer_class=serializers.HelloSerializer
    def get(self,request, format=None):
        """Return a list of APIView features"""
        an_apiview=[
            "uses HTTP methods as function (get,post,patch,put,delete)",
            "is similar to a traditional Django view",
            "gives you the most control over your application logic",
            "is mapped manually to URLS"

        ]
    
        return Response({'message':'hello', 'an_ApiView':an_apiview})
   
   
    def post (self, request):
        """create a hello message with our name"""
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response (serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({"method":'put'})
    

    def patch (self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method":'patch'})

    
    def delete (self, request, pk=None):
        """Delete an object"""
        return Response({"method":'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSET"""

    serializer_class= serializers.HelloSerializer
    def list(self, request):
        """Hello return message"""
        a_viewset=[
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using routers',
            'Provides more functionality with less code',

        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    
    
    def create (self, request):
        """Create a new Hello message"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request,pk=None):
        """Handle getting an object by its id"""
        return Response({'HTTP_method':'GET'})
    
    def update (self, request, pk=None):
        """Handle updating an object"""
        return Response({'HTTP_method':'PUT'})

    def partial_update (self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'HTTP_method':'patch'})

    def destroy (self, request, pk=None):
        """Handle removing an object"""
        return Response({'HTTP_method':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permission.UpdateOwnProfile,)



