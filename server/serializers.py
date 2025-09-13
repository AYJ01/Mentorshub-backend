from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class MentorExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor_Experience
        fields = '__all__'

class MentorEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor_education
        fields = '__all__'

class MentorWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor_works
        fields = '__all__'

class MentorBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor_blogs
        fields = '__all__'

class MentorExperienceImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience_images
        fields = '__all__'

class MentorEducationImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor_education
        fields = '__all__'

class MentorWorksImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_images
        fields = '__all__'

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_details
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'

class CustomerBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_blogs
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class FormImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form_images
        fields = '__all__'

class CustomerReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_review
        fields = '__all__'

class SiteReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site_review
        fields = '__all__'

class CustomerNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_notification
        fields = '__all__'

class MentorNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor_notification
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


