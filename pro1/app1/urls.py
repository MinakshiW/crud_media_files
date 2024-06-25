from django.urls import path
from .views import *

urlpatterns = [
    path('pv/', personview),
    path('sv/', showview),
    path('uv/<pk>/', updateview),
    path('dv/<x>/', deleteview)
]