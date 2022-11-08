from rest_framework import serializers
from django.contrib.auth.models import User

#Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

class userSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =  '__all__'
