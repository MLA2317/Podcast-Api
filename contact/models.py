from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)# agar null tru blank tru qilsa formsisvalid ishlidi aks holda data reuqest postda qolib ketadi
    phone = models.IntegerField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}'s request"


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}'s"
