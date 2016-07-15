from django.db import models

# Create your models here.
from django.utils import timezone
from hitcount.models import HitCount, HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation

class DishPost(models.Model, HitCountMixin):
    DishTitle=models.CharField(max_length=200)
    DishContent=models.TextField(blank=True)
    DishPhoto=models.URLField(blank=True)
    DishCreated_date=models.DateTimeField(auto_now_add=True)
    DishHitcount=GenericRelation(HitCount, object_id_field='object_pk', related_query_name='DishHitcount_relation')
    def __str__(self):
        return self.DishTitle