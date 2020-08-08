from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API VIEW"""

    def get(self,request, format=None):
        """Return a list of APIView features"""
        an_apiview=[
            "uses HTTP methods as function (get,post,patch,put,delete)",
            "is similar to a traditional Django view",
            "gives you the most control over your application logic",
            "is mapped manually to URLS"

        ]

        return Response({'message':'hello', 'an_ApiView':an_apiview})