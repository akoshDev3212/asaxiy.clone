from django.db import models



class Slide(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    
class Products(models.Model):
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE, null=True)
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
    



class Category(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    

class CartItem(models.Model):
    customer = models.ForeignKey('Users.User', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('store.Products', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title
    
    def total_price(self):
        return self.product.price * self.quantity