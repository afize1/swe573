from django.db import models

#save security question and answer for each user

DEMO_CHOICES =(
    ("1", "What is your favorite color"),
    ("2", "What is your favorite book namev"),
    ("3", "What is your favorite song name"),
)

class users(models.Model):
    username= models.CharField(max_length=20)
    security_question = models.CharField(max_length=100)
    answer = models.CharField(max_length=20)
    class Meta:
        db_table='db_users'