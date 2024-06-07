from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/",views.search,name="search"),
    path("search/stocks", views.stocks, name="stocks"),
    path("search/stocks/<str:stockName>",views.getStockDetails,name="stocks"),
    path("register",views.register,name="register"),
    path("checkulogin",views.checkulogin,name="checkulogin"),
]