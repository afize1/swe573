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


class shares(models.Model):
    username=models.CharField(max_length=20)
    subject= models.CharField(max_length=20)
    label = models.CharField(max_length=20)
    private = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    related_subjects = models.CharField(max_length=20)
    value=models.CharField(max_length=20)
    comment = models.CharField(max_length=20)
    class Meta:
        db_table='db_shares'
        
class followUser(models.Model):
    username=models.CharField(max_length=20)
    followers= models.CharField(max_length=20)
    class Meta:
        db_table='db_followers'