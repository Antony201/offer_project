from django.urls import path
from .views import *


app_name = "offer"

urlpatterns = [
    path('offers/create', OfferCreateView.as_view(), name="get_create_offer"),
    path("offers/all", OfferListView.as_view(), name="get_list_offer"),
    path("offers/detail/<int:pk>/", OfferDetailView.as_view(), name="get_delete_update_offer"),

]
