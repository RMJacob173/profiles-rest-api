#from django.shortcuts import render

# Create your views here.
#APIVIEW
from rest_framework.views import APIView
from rest_framework.response import Response # return response from API_VIEW


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIViewFeatures"""
        an_apiview = [
            "User HTTP method as function(get,post,patch,put,delete)",
            "Is similar to a traditional Django View",
            "Gives most control over application logic",
            "Is mapped normally to the urls",
        ]

        return Response({'message':'Hello !', 'an_apiview':an_apiview})
        #converts response obect to json to convert it to json needs list/dictinary
