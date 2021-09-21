from django.urls import path
from . import views


urlpatterns = [
    path('image2text/', views.Image2Text.as_view(), name="image2text"),
    path('image2text/process_image', views.process_image, name="process_image"),


]