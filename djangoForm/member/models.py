from django.db import models

class Member(models.Model):
    firstName = models.CharField(max_length=100, null=True, blank=True, verbose_name="First Name")
    lastName = models.CharField(max_length=100, null=True, blank=True, verbose_name="Lase Name")
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Date Of Birth")
    workPlace = models.CharField(max_length=100, null=True, blank=True, verbose_name="Work Place")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Title")
    tel = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tel")

    def __str__(self):
        return f"{self.firstName} {self.lastName} [{self.workPlace}]"
