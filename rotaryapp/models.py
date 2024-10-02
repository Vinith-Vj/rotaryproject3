from django.db import models

# Create your models here.

class homeCoverImage(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name



class History(models.Model):
    president_name = models.CharField(max_length=400, blank=False)
    president_image=models.ImageField(upload_to='images/',blank=False,null=True)
    secretary_name = models.CharField(max_length=400, blank=False)
    secretary_image=models.ImageField(upload_to='images/',blank=False,null=True)
    start_year = models.IntegerField(blank=False)
    end_year = models.IntegerField(blank=False)

    def __str__(self):
        return f"President---Secretary({self.start_year} - {self.end_year})"
