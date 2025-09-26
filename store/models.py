from django.db import models


class Slide(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title



class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title 
    
    def snippet(self):
        return self.description[:30] + '... read more'
    
    def shorten(self):
        return self.title[:10] + '...'
    

