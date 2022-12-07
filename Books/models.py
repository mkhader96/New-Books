from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Book(models.Model):
    name=models.CharField(max_length=255, null=False, blank=True)
    purchaser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description=models.TextField()
    author = models.CharField(max_length=255, null=False, blank=True)
    cover = models.ImageField(default='https://images.theconversation.com/files/45159/original/rptgtpxd-1396254731.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1356&h=668&fit=crop')
    genre = models.CharField(max_length=255, null=False, blank=True)
    
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Books-list')    

        