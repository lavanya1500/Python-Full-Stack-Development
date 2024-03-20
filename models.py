from django.db import models

class MyModel(models.Model):
    end_year = models.IntegerField()
    intensity = models.IntegerField()
    sector = models.CharField(max_length=255)  
    topic = models.CharField(max_length=255)   # Adjust the max_length according to your data
    insight = models.CharField(max_length=255) # Adjust the max_length according to your data
    url = models.URLField()
    region = models.CharField(max_length=255)  # Adjust the max_length according to your data
    start_year = models.IntegerField()  
    impact = models.CharField(max_length=255)  # Adjust the max_length according to your data
    added = models.CharField(max_length=255)   # Adjust the max_length according to your data
    published = models.CharField(max_length=255)  # Adjust the max_length according to your data
    country = models.CharField(max_length=255)  # Adjust the max_length according to your data
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=255)  # Adjust the max_length according to your data
    source = models.CharField(max_length=255)  # Adjust the max_length according to your data
    title = models.CharField(max_length=255)   # Adjust the max_length according to your data
    likelihood = models.IntegerField()

    # def __str__(self):
    #     return self.sector