from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    publication_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, decimal_places=True, max_digits=8)
    num_pages = models.IntegerField(default=0)
    isbn13 = models.CharField(max_length=12,blank=True, null=True )

    def __str__(self):
        return self.title

