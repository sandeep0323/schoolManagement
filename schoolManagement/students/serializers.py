# serializers.py

from rest_framework import serializers
from .models import Student, Course, StudentCourses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourses
        fields = '__all__'
