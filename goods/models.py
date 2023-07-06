from django.db import models
from django.urls import reverse

from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='media/goods/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-publish_time']


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('index', args=[str(self.pk)])























