from django.urls import path
from .views import generate_graph

urlpatterns = [
    path('graph/', generate_graph, name='generate_graph'),
]
