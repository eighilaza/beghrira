from django.db import models

class Pipeline(models.Model):
    project_name = models.CharField(max_length = 100)
    ihm_port = models.IntegerField()
    slave_port = models.IntegerField()
    def __str__(self):
        return self.project_name
