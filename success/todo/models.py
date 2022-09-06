from django.db import models

class task_db(models.Model):
    task_name = models.CharField(max_length = 200)
    expected_time = models.FloatField()
    actual_time = models.FloatField()

