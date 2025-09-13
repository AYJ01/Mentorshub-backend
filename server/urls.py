from django.urls import path
from . import views

urlpatterns = [
    # ---------------- AUTH & USERS ----------------
    path('users/', views.get_all_users, name='all_users'),
    path('user/create/', views.create_user, name='create_user'),
    path('user/signin/', views.signin, name='signin'),
    path('user/update_usertype/', views.update_usertype, name='update_usertype'),

    # ---------------- MENTORS ----------------
    path('mentors/', views.all_mentors, name='all_mentors'),
    path('mentor/<int:pk>/', views.mentor_profile, name='mentor_profile'),
    path('mentor/<int:pk>/edit/', views.edit_mentor_profile, name='edit_mentor_profile'),

    # Mentor Blogs
    path('mentor/<int:mentor_id>/blogs/add/', views.add_blog, name='add_blog'),
    path('mentor/blog/<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),
    path('mentor/blog/<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),

    # Mentor Experiences
    path('mentor/<int:mentor_id>/experience/add/', views.add_experience, name='add_experience'),
    path('experience/<int:exp_id>/edit/', views.edit_experience, name='edit_experience'),
    path('experience/<int:exp_id>/delete/', views.delete_experience, name='delete_experience'),

    # Mentor Education
    path('mentor/<int:mentor_id>/education/add/', views.add_education, name='add_education'),
    path('education/<int:edu_id>/edit/', views.edit_education, name='edit_education'),
    path('education/<int:edu_id>/delete/', views.delete_education, name='delete_education'),

    # Mentor Works
    path('mentor/<int:mentor_id>/work/add/', views.add_work, name='add_work'),
    path('work/<int:work_id>/edit/', views.edit_work, name='edit_work'),
    path('work/<int:work_id>/delete/', views.delete_work, name='delete_work'),

    # Mentor Reviews
    path('mentor/<int:mentor_id>/reviews/', views.mentor_reviews, name='mentor_reviews'),
    path('mentor/<int:mentor_id>/review/<int:customer_id>/add/', views.add_review, name='add_review'),

    # Mentor Notifications
    path('mentor/<int:mentor_id>/notifications/', views.mentor_notifications, name='mentor_notifications'),
    path('mentor/<int:mentor_id>/notifications/add/', views.add_mentor_notification, name='add_mentor_notification'),

    # ---------------- CUSTOMERS ----------------
    path('customers/', views.all_customers, name='all_customers'),
    path('customer/<int:pk>/', views.customer_profile, name='customer_profile'),
    path('customer/<int:pk>/edit/', views.edit_customer_profile, name='edit_customer_profile'),

    # Customer Blogs
    path('customer/<int:customer_id>/blogs/add/', views.add_customer_blog, name='add_customer_blog'),
    path('customer/blog/<int:blog_id>/edit/', views.edit_customer_blog, name='edit_customer_blog'),
    path('customer/blog/<int:blog_id>/delete/', views.delete_customer_blog, name='delete_customer_blog'),

    # Customer Achievements
    path('customer/<int:customer_id>/achievement/add/', views.add_achievement, name='add_achievement'),
    path('achievement/<int:ach_id>/edit/', views.edit_achievement, name='edit_achievement'),
    path('achievement/<int:ach_id>/delete/', views.delete_achievement, name='delete_achievement'),

    # Customer Notifications
    path('customer/<int:customer_id>/notifications/', views.customer_notifications, name='customer_notifications'),
    path('customer/<int:customer_id>/notifications/add/', views.add_customer_notification, name='add_customer_notification'),

    # ---------------- CHAT ----------------
    path('chat/<int:customer_id>/<int:mentor_id>/', views.get_chat, name='get_chat'),
    path('chat/<int:customer_id>/<int:mentor_id>/send/', views.send_message, name='send_message'),
]
