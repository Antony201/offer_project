from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Offer, Client, Responsible
from .serializers import OfferListSerializer


class CRUDTest(APITestCase):
    def setUp(self):
        self.Client = Client.objects.create(fio="Василенко Василий Петрович",
                                            phone="+79333333"
                                        )

        self.Responsible = Responsible.objects.create(fio="Михаленко Василий Петрович",
                                                      position="слесарь"
                                                )

        self.offer = Offer.objects.create(text="Simple text",
                                          responsible=self.Responsible,
                                          client=self.Client
                                    )


    def test_create_offer(self):
        url = reverse("offer:get_create_offer")

        data = {
            "text": "Hello world",
            "responsible": self.Responsible.pk,
            "client": self.Client.pk

        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_offer(self):
        url = reverse("offer:get_delete_update_offer", kwargs={"pk" : self.offer.pk})

        data = {
            "text": "It's updated text!",
            "responsible": self.Responsible.pk,
            "client": self.Client.pk,
        }

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Offer.objects.get(id=self.offer.id).text, "It's updated text!")


    def test_delete_offer(self):
        url = reverse("offer:get_delete_update_offer", kwargs={"pk": self.offer.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_read_offer(self):
        url = reverse("offer:get_list_offer")
        response = self.client.get(url)

        offers = Offer.objects.all()
        serializer = OfferListSerializer(offers, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

