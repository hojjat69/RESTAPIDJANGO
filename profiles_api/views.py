from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
            status=status.HTTP_400_BAD_REQUEST
            )

    
    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({"method":'put'})
    

    def patch (self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method":'patch'})

    
    def delete (self, request, pk=None):
        """Delete an object"""
        return Response({"method":'delete'})

