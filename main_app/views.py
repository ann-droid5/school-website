from django.shortcuts import render
from .models import HeroSlide, AboutSection, StudentLife, NewsArticle, GalleryImage, Footer

def index(request):
    slides = HeroSlide.objects.all()
    about = AboutSection.objects.first()
    student_life = StudentLife.objects.first()
    news = NewsArticle.objects.all().order_by('-id')[:4]
    gallery = GalleryImage.objects.all()
    footer = Footer.objects.first()

    context = {
        'slides': slides,
        'about': about,
        'student_life': student_life,
        'news': news,
        'gallery': gallery,
        'footer': footer,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def academics(request):
    return render(request, 'academics.html')

def admissions(request):
    return render(request, 'admissions.html')



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
