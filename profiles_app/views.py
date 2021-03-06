#from django.shortcuts import render

# Create your views here.
#APIVIEW
from rest_framework.views import APIView
from rest_framework.response import Response # return response from API_VIEW

#Other APIVIEW methods POST,PATH....
from rest_framework import status #list of HTTP status used when returning the response from API
from profiles_app import serializers

# to use apiviewset
from rest_framework import viewsets

#for the ModelSerializer importing models
from profiles_app import models

#permissions for the ViewSet
from rest_framework.authentication import TokenAuthentication
from profiles_app import permissions


#to apply filters
from rest_framework import filters

#use token authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#to set permissions on profile
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

#to restrict access to those who only have accounts
from rest_framework.permissions import IsAuthenticated

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


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""
    #to get the input
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return Hello Message"""
        a_viewset=[
            "Uses action (list, create, retrieve, update, partial_update)",
            "Atomatically maps to the irls using routers",
            "provides more functionality with less code"
        ]
        return Response({'messgae':"Hello", "a_viewset":a_viewset})

    def create(self, request):
        """New hello messgae"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting object by ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating art of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #Code to assign authentication
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields =("name","email")

class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creation and updation of feed """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    #to set permissions
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticated)

    def perform_create(self,serializer):
        """Sets the user profile to logged in user"""
        serializer.save(user_profile= self.request.user)
