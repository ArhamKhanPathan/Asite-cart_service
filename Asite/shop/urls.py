# from django.contrib import admin
from .import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("product/<int:myid>", views.prodView, name="prodView"),
    path("checkout/", views.checkout, name="CheckOut"),
]