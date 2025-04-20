from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=70)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # Many-to-One ilişki

    def __str__(self):
        return self.title