from django.db import models
import json

def default_grid():
    return json.dumps([["" for _ in range(30)] for _ in range(10)])  # Grid 10 rows x 30 columns

class TestForm(models.Model):
    data = models.JSONField(default=default_grid)  # Using a callable for default
    notes = models.TextField(blank=True)
