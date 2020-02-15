#from django.shortcuts import render

# Create your views here.
#APIVIEW
from rest_framework.views import APIView
from rest_framework.response import Response # return response from API_VIEW
#Other APIVIEW methods POST,PATH....
from rest_framework import status #list of HTTP status used when returning the response from API
from profiles_app import serializers
# to use apiviewset
from rest_framework import viewset




class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

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


    def post(self,request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data = request.data)#returns the configured serializer class
        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )


    def put(self, request,pk=None):
        """Handles updating an object"""
        return Response({'method':"PUT"})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method':"PATCH"})

    def delete(self,request, pk =None):
        """Handle deleting an object"""
        return Response({'method':"DELETE"})
