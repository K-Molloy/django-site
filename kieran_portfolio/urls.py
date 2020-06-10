from django.urls import path
from kieran_portfolio.views import kieran_portfolio_view

urlpatterns = [

    path('', kieran_portfolio_view, name='kieran'),
]