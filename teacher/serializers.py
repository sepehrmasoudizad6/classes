from rest_framework import serializers
from .models import *

class AddTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('username', 'password', 'first_name', 'last_name', 'national_code', 'school_name', 'biography')
     
    
    def validate_national_code(self, value):
        message = 'Your entered national code is invalid.'
        if len(value) != 10:
            raise serializers.ValidationError(message)
        try:
            if int(value) <= 0:
                raise serializers.ValidationError(message)
        except:
            raise serializers.ValidationError(message)
        return value    

class AddNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('teacher', 'title', 'context')
    





        
    