from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    order = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
    
    @property
    def getArticles(self):
        return Article.objects.filter(category = self.id).order_by('order')
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    # time_create = models.DateTimeField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    order = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title
