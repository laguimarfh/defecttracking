import json
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Sheet(models.Model):
    """
    Represents a Defect Tracking
    """
    PROCESS_CHOICES = [
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
        ('S8', 'S8'),
        ('S9', 'S9'),
        ('S10', 'S10'),
        ('S11', 'S2'),
        ('S12', 'S2'),
        ('ED', 'ED'),
    ]
    DEFECT_CHOICES = [
        ('XS' , 'Excess'),
        ('WL' , 'Waterleak'),
        ('PH' , 'Pin Hole'),
        ('F' , 'Flick'),
        ('ED R' , 'ED run'),
        ('ED B' , 'ED Blister'),
        ('NS' , 'No Spat'),
        ('OF' , 'Off Location'),
        ('MC' , 'Missing Clip'),
        ('PA' , 'Poor Application'),
        ('NB' , 'No Brush'),
        ('G' , 'Gap'),
        ('MAS' , 'Mastic'),
        ('BB' , 'Body Bound'),
    ]
    process = models.CharField(max_length=30, choices=PROCESS_CHOICES, null=False)
    defect = models.CharField(max_length=30, choices=DEFECT_CHOICES, null=False)
    # location = models.CharField(max_length=50, null=False )
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    period = models.CharField(max_length=30, null=False, choices=[('1st', '1st'), ('2nd','2nd'), ('3rd','3rd'), ('4th','4th')])
    coorx = models.FloatField(null=True, blank=True, default=None)
    coory = models.FloatField(null=True, blank=True, default=None)
    count_day = models.IntegerField(null=True, blank=True, default=None)


class Post(models.Model):
    """
    Represents a Defect Tracking
    """
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    coord = models.TextField()

    # Time is a rhinocerous
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text+' - '+self.author.username


class AjaxImage(models.Model):
    image_coord = models.FloatField()

    def __str__(self):
        return self.image_coord


#  ('S1', 'RS Mohican Channel'), 
#         ('S2', 'RS Mohican Channel') , 
#         ('S3', 'RS Firewall and Door Beads'),
#         ('S4', 'LS Firewall and Door Beads'),
#         ('S5', 'RS Rear Door and Hatch Hinge'),
#         ('S6', 'LS Rear Door and Hatch Hinge'),
#         ('S7', 'RS Front Door and Trunck Brush'),
#         ('S8', 'LS Front Door and Trunck Brush'),
#         ('S9', 'RS HATCH and HOOD'),
#         ('S10', 'LS HATCH and HOOD'), 
#         ('S11', 'RS Lower Trough and Body Combi'),
#         ('S12', 'RS Lower Trough and Body Combi'),