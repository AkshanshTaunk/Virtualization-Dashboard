from django.db import models


class DashboardData(models.Model):
    end_year = models.CharField(max_length=10, blank=True, null=True)
    intensity = models.IntegerField(null=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=10, blank=True, null=True)
    impact = models.CharField(max_length=100, blank=True, null=True)
    added = models.CharField(max_length=50, blank=True, null=True)
    published = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField(null=True)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    

