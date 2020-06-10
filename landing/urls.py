from django.urls import path
from landing.views import landing_view

urlpatterns = [

    path('', landing_view, name='landing'),
]