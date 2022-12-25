from django.db import models

#save security question and answer for each user

DEMO_CHOICES =(
    ("1", "What is your favorite color"),
    ("2", "What is your favorite book namev"),
    ("3", "What is your favorite song name"),
)

class users(models.Model):
    username= models.CharField(max_length=255)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    security_question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    occupation= models.CharField(max_length=255)
    interest= models.CharField(max_length=255)
    bio= models.CharField(max_length=255)
    followings = models.IntegerField()
    followers = models.IntegerField()
    class Meta:
        db_table='db_users'
        
class images(models.Model):
    username= models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    class Meta:
        db_table='db_images'

class shares(models.Model):
    username=models.CharField(max_length=255)
    subject= models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    private = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    content=models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    class Meta:
        db_table='db_shares'
        
class followUser(models.Model):
    username=models.CharField(max_length=255)
    followers= models.CharField(max_length=255)
    class Meta:
        db_table='db_followers'
        
class postComment(models.Model):
    post_id=models.IntegerField();
    username=models.CharField(max_length=255)
    comment= models.CharField(max_length=255)
    class Meta:
        db_table='db_post_comment'