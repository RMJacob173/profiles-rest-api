from django.urls import path, include
from profiles_app import views
#include router module to handle ViewSet
from rest_framework.routers import DefaultRouter

#adding routers to handel ViewSet
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet,base_name = 'hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('', include(router.urls)), ##'' assign no prefix to the url includes all url in the bas url file
]
