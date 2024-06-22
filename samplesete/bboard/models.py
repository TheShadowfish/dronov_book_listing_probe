from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(**NULLABLE)
    price = models.FloatField(**NULLABLE)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
