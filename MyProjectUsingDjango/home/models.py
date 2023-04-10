from django.db import models

# Create your models here. ZModels are something that defines one's database
# makemigrations - create changes and store it in a file
# migrate - apply the pending changes created by makemigrations 
class Contact(models.Model):        #just like atable that holds data
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name