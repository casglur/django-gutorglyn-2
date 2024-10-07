
from django.db import models
from django.db.models.aggregates import Max

class manuscripts(models.Model):
    poem_number = models.CharField(max_length=200)
    control = models.CharField(max_length=200)    
    manuscript_control = models.CharField(max_length=200)
    manuscript = models.CharField(max_length=200)    
    manuscript_ref = models.CharField(max_length=200)
    hand_cy = models.CharField(max_length=200)
    dates_cy = models.CharField(max_length=200)   
    hand_en = models.CharField(max_length=200)
    dates_en = models.CharField(max_length=200)

class manuscriptSort(models.Model):    
    manuscript_name = models.CharField(max_length=100)
    sort_order = models.IntegerField()           

class patronsAndPoets(models.Model):
    note_id = models.CharField(max_length=200)
    poem_ids = models.CharField(max_length=200)
    title_cym = models.CharField(max_length=200)
    title_eng = models.CharField(max_length=200)    
    
class personalNames(models.Model):
    line_ref = models.CharField(max_length=20)
    name_id = models.CharField(max_length=5)
    name_type = models.CharField(max_length=7)
    name_in_text = models.CharField(max_length=30)
    def_cym = models.CharField(max_length=255)
    def_eng = models.CharField(max_length=255)     
    poem_number = models.CharField(max_length=5)
   
class placeNames(models.Model):
    line_ref = models.CharField(max_length=10)
    place_id = models.CharField(max_length=5)
    place_type = models.CharField(max_length=5)
    place_in_text = models.CharField(max_length=30)
    def_cym = models.CharField(max_length=255)
    def_eng = models.CharField(max_length=255)    
    poem_number = models.CharField(max_length=5)
    cross_ref_text = models.CharField(max_length=255,blank=True)
    cross_ref_id = models.CharField(max_length=10,blank=True)
    
class poemSort(models.Model):    
    poem_number = models.CharField(max_length=4)
    sort_order = models.DecimalField(max_digits=5, decimal_places=1)
    
