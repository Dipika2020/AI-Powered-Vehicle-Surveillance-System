from django.db import models

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20)
    image_path = models.CharField(max_length=200)
    detected_at = models.DateTimeField(auto_now_add=True)

class LaneDetection(models.Model):
    image_path = models.CharField(max_length=200)
    detected_at = models.DateTimeField(auto_now_add=True)
