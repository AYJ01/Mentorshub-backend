from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# ---------------- ROOT ----------------
@api_view(['GET'])
def index(request):
    return JsonResponse({"message": "Welcome to Mentors Hub API"})


# ---------------- USER AUTH ----------------
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    return JsonResponse(UserSerializer(users, many=True).data, safe=False)

@api_view(['POST'])
def create_user(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )
        return JsonResponse(UserSerializer(user).data, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['POST'])
def signin(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.get(email=data['email'])
        if user.check_password(data['password']):
            return JsonResponse(UserSerializer(user).data, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

@api_view(['PUT'])
def update_usertype(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.get(id=data['userid'])
        user.usertype = data['usertype']
        user.save()
        if user.usertype == 'mentor':
            Mentor.objects.get_or_create(user=user)
        else:
            Customer_details.objects.get_or_create(user=user)
        return JsonResponse(UserSerializer(user).data, status=200)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


# ---------------- MENTORS ----------------
@api_view(['GET'])
def all_mentors(request):
    mentors = Mentor.objects.all()
    return JsonResponse(MentorSerializer(mentors, many=True).data, safe=False)

@api_view(['GET'])
def mentor_profile(request, pk):
    try:
        mentor = Mentor.objects.get(id=pk)
        return JsonResponse(MentorSerializer(mentor).data, safe=False)
    except Mentor.DoesNotExist:
        return JsonResponse({"error": "Mentor not found"}, status=404)

@api_view(['PUT'])
def edit_mentor_profile(request, pk):
    try:
        mentor = Mentor.objects.get(id=pk)
        for field in ['bio', 'address', 'phone_number', 'specialized_in', 'rating']:
            if field in request.data:
                setattr(mentor, field, request.data[field])
        mentor.save()
        return JsonResponse(MentorSerializer(mentor).data, safe=False)
    except Mentor.DoesNotExist:
        return JsonResponse({"error": "Mentor not found"}, status=404)


# ---------------- CUSTOMERS ----------------
@api_view(['GET'])
def all_customers(request):
    customers = Customer_details.objects.all()
    return JsonResponse(CustomerDetailsSerializer(customers, many=True).data, safe=False)

@api_view(['GET'])
def customer_profile(request, pk):
    try:
        customer = Customer_details.objects.get(id=pk)
        return JsonResponse(CustomerDetailsSerializer(customer).data, safe=False)
    except Customer_details.DoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status=404)

@api_view(['PUT'])
def edit_customer_profile(request, pk):
    try:
        customer = Customer_details.objects.get(id=pk)
        for field in ['address', 'phone_number', 'about']:
            if field in request.data:
                setattr(customer, field, request.data[field])
        if 'profile_picture' in request.FILES:
            customer.profile_picture = request.FILES['profile_picture']
        if 'cover_image' in request.FILES:
            customer.cover_image = request.FILES['cover_image']
        customer.save()
        return JsonResponse(CustomerDetailsSerializer(customer).data, safe=False)
    except Customer_details.DoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status=404)


# ---------------- BLOGS ----------------
@api_view(['POST'])
def add_blog(request, mentor_id):
    mentor = Mentor.objects.get(id=mentor_id)
    blog = Mentor_blogs.objects.create(
        mentor=mentor,
        title=request.data.get('title'),
        content=request.data.get('content'),
        image=request.FILES.get('image')
    )
    return JsonResponse(MentorBlogsSerializer(blog).data, status=201)

@api_view(['PUT'])
def edit_blog(request, blog_id):
    try:
        blog = Mentor_blogs.objects.get(id=blog_id)
        for field in ['title', 'content']:
            if field in request.data:
                setattr(blog, field, request.data[field])
        if 'image' in request.FILES:
            blog.image = request.FILES['image']
        blog.save()
        return JsonResponse(MentorBlogsSerializer(blog).data, safe=False)
    except Mentor_blogs.DoesNotExist:
        return JsonResponse({"error": "Blog not found"}, status=404)

@api_view(['DELETE'])
def delete_blog(request, blog_id):
    try:
        blog = Mentor_blogs.objects.get(id=blog_id)
        blog.delete()
        return JsonResponse({"message": "Blog deleted"}, status=204)
    except Mentor_blogs.DoesNotExist:
        return JsonResponse({"error": "Blog not found"}, status=404)


# ---------------- EXPERIENCES ----------------
@api_view(['POST'])
def add_experience(request, mentor_id):
    mentor = Mentor.objects.get(id=mentor_id)
    exp = Mentor_Experience.objects.create(
        mentor=mentor,
        company_name=request.data.get("company_name"),
        role=request.data.get("role"),
        start_date=request.data.get("start_date"),
        end_date=request.data.get("end_date"),
        description=request.data.get("description"),
    )
    return JsonResponse(MentorExperienceSerializer(exp).data, status=201)

@api_view(['PUT'])
def edit_experience(request, exp_id):
    try:
        exp = Mentor_Experience.objects.get(id=exp_id)
        for field in ['company_name', 'role', 'start_date', 'end_date', 'description']:
            if field in request.data:
                setattr(exp, field, request.data[field])
        exp.save()
        return JsonResponse(MentorExperienceSerializer(exp).data, safe=False)
    except Mentor_Experience.DoesNotExist:
        return JsonResponse({"error": "Experience not found"}, status=404)

@api_view(['DELETE'])
def delete_experience(request, exp_id):
    try:
        exp = Mentor_Experience.objects.get(id=exp_id)
        exp.delete()
        return JsonResponse({"message": "Experience deleted"}, status=204)
    except Mentor_Experience.DoesNotExist:
        return JsonResponse({"error": "Experience not found"}, status=404)


# ---------------- EDUCATION ----------------
@api_view(['POST'])
def add_education(request, mentor_id):
    mentor = Mentor.objects.get(id=mentor_id)
    edu = Mentor_education.objects.create(
        mentor=mentor,
        degree=request.data.get("degree"),
        institution=request.data.get("institution"),
        start_date=request.data.get("start_date"),
        end_date=request.data.get("end_date"),
        description=request.data.get("description"),
    )
    return JsonResponse(MentorEducationSerializer(edu).data, status=201)

@api_view(['PUT'])
def edit_education(request, edu_id):
    try:
        edu = Mentor_education.objects.get(id=edu_id)
        for field in ['degree', 'institution', 'start_date', 'end_date', 'description']:
            if field in request.data:
                setattr(edu, field, request.data[field])
        edu.save()
        return JsonResponse(MentorEducationSerializer(edu).data, safe=False)
    except Mentor_education.DoesNotExist:
        return JsonResponse({"error": "Education not found"}, status=404)

@api_view(['DELETE'])
def delete_education(request, edu_id):
    try:
        edu = Mentor_education.objects.get(id=edu_id)
        edu.delete()
        return JsonResponse({"message": "Education deleted"}, status=204)
    except Mentor_education.DoesNotExist:
        return JsonResponse({"error": "Education not found"}, status=404)


# ---------------- WORKS ----------------
@api_view(['POST'])
def add_work(request, mentor_id):
    mentor = Mentor.objects.get(id=mentor_id)
    work = Mentor_works.objects.create(
        mentor=mentor,
        title=request.data.get("title"),
        description=request.data.get("description"),
        start_date=request.data.get("start_date"),
        end_date=request.data.get("end_date"),
    )
    return JsonResponse(MentorWorksSerializer(work).data, status=201)

@api_view(['PUT'])
def edit_work(request, work_id):
    try:
        work = Mentor_works.objects.get(id=work_id)
        for field in ['title', 'description', 'start_date', 'end_date']:
            if field in request.data:
                setattr(work, field, request.data[field])
        work.save()
        return JsonResponse(MentorWorksSerializer(work).data, safe=False)
    except Mentor_works.DoesNotExist:
        return JsonResponse({"error": "Work not found"}, status=404)

@api_view(['DELETE'])
def delete_work(request, work_id):
    try:
        work = Mentor_works.objects.get(id=work_id)
        work.delete()
        return JsonResponse({"message": "Work deleted"}, status=204)
    except Mentor_works.DoesNotExist:
        return JsonResponse({"error": "Work not found"}, status=404)


# ---------------- ACHIEVEMENTS ----------------
@api_view(['POST'])
def add_achievement(request, customer_id):
    customer = Customer_details.objects.get(id=customer_id)
    ach = Achievements.objects.create(
        customer=customer,
        title=request.data.get("title"),
        description=request.data.get("description"),
        date=request.data.get("date"),
    )
    return JsonResponse(AchievementSerializer(ach).data, status=201)

@api_view(['PUT'])
def edit_achievement(request, ach_id):
    try:
        ach = Achievements.objects.get(id=ach_id)
        for field in ['title', 'description', 'date']:
            if field in request.data:
                setattr(ach, field, request.data[field])
        ach.save()
        return JsonResponse(AchievementSerializer(ach).data, safe=False)
    except Achievements.DoesNotExist:
        return JsonResponse({"error": "Achievement not found"}, status=404)

@api_view(['DELETE'])
def delete_achievement(request, ach_id):
    try:
        ach = Achievements.objects.get(id=ach_id)
        ach.delete()
        return JsonResponse({"message": "Achievement deleted"}, status=204)
    except Achievements.DoesNotExist:
        return JsonResponse({"error": "Achievement not found"}, status=404)


# ---------------- REVIEWS ----------------
@api_view(['POST'])
def add_review(request, mentor_id, customer_id):
    mentor = Mentor.objects.get(id=mentor_id)
    customer = Customer_details.objects.get(id=customer_id)
    review = Customer_review.objects.create(
        customer=customer,
        mentor=mentor,
        rating=request.data.get("rating"),
        comment=request.data.get("comment"),
    )
    return JsonResponse(CustomerReviewsSerializer(review).data, status=201)

@api_view(['GET'])
def mentor_reviews(request, mentor_id):
    reviews = Customer_review.objects.filter(mentor_id=mentor_id)
    return JsonResponse(CustomerReviewsSerializer(reviews, many=True).data, safe=False)


# ---------------- CHAT ----------------
@api_view(['POST'])
def send_message(request, customer_id, mentor_id):
    customer = Customer_details.objects.get(id=customer_id)
    mentor = Mentor.objects.get(id=mentor_id)
    chat = Chat.objects.create(
        customer=customer,
        mentor=mentor,
        sender=request.data.get("sender"),
        message=request.data.get("message"),
    )
    return JsonResponse(ChatSerializer(chat).data, status=201)

@api_view(['GET'])
def get_chat(request, customer_id, mentor_id):
    messages = Chat.objects.filter(customer_id=customer_id, mentor_id=mentor_id).order_by("created_at")
    return JsonResponse(ChatSerializer(messages, many=True).data, safe=False)


# ---------------- NOTIFICATIONS ----------------
@api_view(['POST'])
def add_customer_notification(request, customer_id):
    customer = Customer_details.objects.get(id=customer_id)
    notif = Customer_notification.objects.create(
        customer=customer,
        message=request.data.get("message")
    )
    return JsonResponse(CustomerNotificationsSerializer(notif).data, status=201)

@api_view(['POST'])
def add_mentor_notification(request, mentor_id):
    mentor = Mentor.objects.get(id=mentor_id)
    notif = Mentor_notification.objects.create(
        mentor=mentor,
        message=request.data.get("message")
    )
    return JsonResponse(MentorNotificationsSerializer(notif).data, status=201)

@api_view(['GET'])
def customer_notifications(request, customer_id):
    notifs = Customer_notification.objects.filter(customer_id=customer_id)
    return JsonResponse(CustomerNotificationsSerializer(notifs, many=True).data, safe=False)

@api_view(['GET'])
def mentor_notifications(request, mentor_id):
    notifs = Mentor_notification.objects.filter(mentor_id=mentor_id)
    return JsonResponse(MentorNotificationsSerializer(notifs, many=True).data, safe=False)

@api_view(['POST'])
def add_customer_blog(request, customer_id):
    try:
        customer = Customer_details.objects.get(id=customer_id)
        blog = Customer_blogs.objects.create(
            customer=customer,
            title=request.data.get("title"),
            content=request.data.get("content"),
        )
        return JsonResponse(CustomerBlogsSerializer(blog).data, status=201)
    except Customer_details.DoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status=404)

# --------- EDIT CUSTOMER BLOG ---------
@api_view(['PUT'])
def edit_customer_blog(request, blog_id):
    try:
        blog = Customer_blogs.objects.get(id=blog_id)
        if "title" in request.data:
            blog.title = request.data["title"]
        if "content" in request.data:
            blog.content = request.data["content"]
        blog.save()
        return JsonResponse(CustomerBlogsSerializer(blog).data, safe=False)
    except Customer_blogs.DoesNotExist:
        return JsonResponse({"error": "Customer blog not found"}, status=404)

# --------- DELETE CUSTOMER BLOG ---------
@api_view(['DELETE'])
def delete_customer_blog(request, blog_id):
    try:
        blog = Customer_blogs.objects.get(id=blog_id)
        blog.delete()
        return JsonResponse({"message": "Customer blog deleted successfully"}, status=204)
    except Customer_blogs.DoesNotExist:
        return JsonResponse({"error": "Customer blog not found"}, status=404)