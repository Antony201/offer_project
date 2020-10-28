from django.db import models

class Responsible(models.Model):
    fio = models.CharField(max_length=255)
    position = models.CharField(max_length=40)

    def __str__(self):
        return self.fio

class Client(models.Model):
    fio = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.fio

class Offer(models.Model):
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"offer_{self.id}"