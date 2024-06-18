from rest_framework import serializers
from .models import Student

# Validetor Fuction
def name_length(value):
    if len(value) < 3:
        raise serializers.ValidationError('Name should have at least 3 charecter')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[name_length])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance


    # Field level validation
    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('Sorry...Seats Full')
        
        return value

    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'rahat' and ct.lower() != 'dhaka':
            raise serializers.ValidationError('City must be Dhaka')
        return data
