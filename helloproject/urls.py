from django.urls import path
from helloapp.views import hello_world

urlpatterns = [
    path('', hello_world),
]
