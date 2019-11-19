from django.db import models

# models are basically database in SQLite. We can change it to any other database we like by changing the settings.py

class Question(models.Model):
    question    = models.TextField()
    answer      = models.TextField()
    options     = models.TextField()    #We can change to models.ListCharField() in django_mysql.models
    weight      = models.IntegerField(default=1)