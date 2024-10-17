# from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class data(models.Model):
    # fields of the model
    name = models.CharField(max_length = 100)
    collage_name = models.CharField(max_length = 100)
    parent_number = models.IntegerField(max_length = 10)
    parent_email = models.EmailField()
    student_email = models.EmailField()
    percentage = models.IntegerField()
    practical_mark = models.IntegerField()
    extra_act_mark= models.IntegerField()


    def __str__(self): 
        return self.name 