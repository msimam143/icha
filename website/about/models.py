from django.db import models


class pribadi(models.Model):
    nama = models.CharField(max_length=50)

    def _str_(self):
        return self.nama

# Create your models here.

