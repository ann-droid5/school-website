from django.shortcuts import render

# Create your views here.
# main_app/views.py
from django.shortcuts import render
from .models import About, GalleryImage




def index(request):
    return render(request, 'index.html')

def about(request):
    about = About.objects.first()  # get the first About entry from the database
    return render(request, 'about.html', {'about': about})

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def academics(request):
    return render(request, 'academics.html')

def admissions(request):
    return render(request, 'admissions.html')

def alumni(request):
    return render(request, 'alumni.html')

def campus_facilities(request):
    return render(request, 'campus-facilities.html')

def faculty_staff(request):
    return render(request, 'faculty-staff.html')

def students_life(request):
    return render(request, 'students-life.html')

def event_details(request):
    return render(request, 'event-details.html')

def news(request):
    return render(request, 'news.html')

def news_details(request):
    return render(request, 'news-details.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms_of_service(request):
    return render(request, 'terms-of-service.html')
