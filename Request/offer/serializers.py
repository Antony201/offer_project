from rest_framework import serializers

from .models import Offer, Client, Responsible


class BaseOfferSerializer(serializers.Serializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)


class ResponsibleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = "__all__"


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"



class OfferListSerializer(serializers.ModelSerializer, BaseOfferSerializer):
    client = ClientCreateSerializer()
    responsible = ResponsibleCreateSerializer()

    class Meta:
        model = Offer
        fields = ("id", "text", "date", "responsible", "client")


class OfferDetailSerializer(serializers.ModelSerializer, BaseOfferSerializer):
    client_info = ClientCreateSerializer(source="client", read_only=True)

    class Meta:
        model = Offer
        fields = ("id", "text", "date", "responsible", "client", "client_info")


class OfferCreateSerializer(serializers.ModelSerializer, BaseOfferSerializer):
    client_info = ClientCreateSerializer(source="client", read_only=True)

    class Meta:
        model = Offer
        fields = ("id", "text", "date", "responsible", "client", "client_info")
