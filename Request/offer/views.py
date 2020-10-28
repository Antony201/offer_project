from rest_framework.response import Response
from rest_framework import generics

from django.views.decorators.cache import cache_page

from .models import Offer
from .serializers import *


class OfferCreateView(generics.CreateAPIView):
    serializer_class = OfferCreateSerializer


class OfferListView(generics.ListAPIView):
    cash = cache_page(timeout=60*15)
    serializer_class = OfferListSerializer
    queryset = Offer.objects.select_related("responsible").select_related("client")


class OfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    cash = cache_page(timeout=60 * 15)
    serializer_class = OfferDetailSerializer
    queryset = Offer.objects.select_related("responsible").select_related("client").all()

