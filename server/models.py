from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    usertype=models.CharField(max_length=50,null=True)

    class Meta:
        db_table = 'user'

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    specialized_in = models.TextField(null=True)
    rating = models.FloatField(null=True)

    class Meta:
        db_table = 'mentor'


class Mentor_Experience(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField(null=True)
    profile = models.ImageField(upload_to='mentor_profiles/', null=True)
    cover_image = models.ImageField(upload_to='mentor_cover_images/', null=True)

    class Meta:
        db_table = 'mentor_experience'


class Experience_images(models.Model):
    experience = models.ForeignKey(Mentor_Experience, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='experience_images/')

    class Meta:
        db_table = 'experience_images'


class Mentor_education(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255, null=True)
    institution = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'mentor_education'


class Mentor_works(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    class Meta:
        db_table = 'mentor_works'


class Work_images(models.Model):
    work = models.ForeignKey(Mentor_works, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='work_images/')

    class Meta:
        db_table = 'work_images'


class Mentor_blogs(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='mentor_blogs/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mentor_blogs'


class Customer_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    about = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)
    cover_image = models.ImageField(upload_to='cover_images/', null=True)

    class Meta:
        db_table = 'customer_details'


class Achievements(models.Model):
    customer = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)

    class Meta:
        db_table = 'achievements'


class Customer_blogs(models.Model):
    customer = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customer_blogs'


class Tasks(models.Model):
    customer = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    task = models.TextField(null=True)
    result = models.TextField(null=True)
    message = models.TextField(null=True)
    feel = models.TextField(null=True)
    optional = models.BooleanField(default=False)

    class Meta:
        db_table = 'tasks'


class Form(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    question = models.TextField(null=True)
    answer = models.TextField(null=True)
    optional = models.BooleanField(default=False)

    class Meta:
        db_table = 'form'


class Form_images(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='form_images/')

    class Meta:
        db_table = 'form_images'


class Customer_review(models.Model):
    customer = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customer_review'


class Site_review(models.Model):
    customer = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'site_review'


class Customer_notification(models.Model):
    customer = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customer_notification'


class Mentor_notification(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mentor_notification'


class Chat(models.Model):
    customer = models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    sender = models.TextField(null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat'

