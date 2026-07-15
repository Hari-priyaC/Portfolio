from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import ContactMessageForm
from .models import Certificate, Education, Experience, Profile, Project, SkillCategory, Skill


def index(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(
            name="Haripriya C",
            title="Python Backend Developer",
            bio="I build scalable backend systems with Django, FastAPI, and modern cloud-native practices.",
            email="haripriya@example.com",
        )

    skill_categories = SkillCategory.objects.prefetch_related("skills").all()
    projects = Project.objects.all().order_by("id")
    experiences = Experience.objects.all().order_by("start_date")
    educations = Education.objects.all().order_by("id")
    certificates = Certificate.objects.all().order_by("issued_on")
    services = [
        {"title": "Backend Development", "description": "Enterprise-grade backend systems and services.", "icon": "fas fa-server"},
        {"title": "REST API Development", "description": "Reliable, secure APIs with solid contracts and documentation.", "icon": "fas fa-code"},
        {"title": "Web Application Development", "description": "Full-stack product development with polished UX.", "icon": "fas fa-laptop-code"},
        {"title": "Database Design", "description": "Normalized schemas, performance tuning, and migrations.", "icon": "fas fa-database"},
        {"title": "Performance Optimization", "description": "Improved latency, caching, and scalable architecture.", "icon": "fas fa-tachometer-alt"},
        {"title": "Deployment", "description": "Docker, Linux, Nginx, and cloud hosting readiness.", "icon": "fas fa-cloud"},
    ]
    testimonials = [
        {"quote": "The backend architecture was thoughtful, secure, and scalable from day one.", "author": "Ananya Rao", "role": "Product Lead"},
        {"quote": "The delivery was fast, polished, and production-ready.", "author": "Manish Verma", "role": "Engineering Manager"},
    ]
    about_tags = ["Python", "Django", "FastAPI", "PostgreSQL", "Redis", "Docker", "Kafka", "Celery"]
    form = ContactMessageForm()
    return render(
        request,
        "index.html",
        {
            "profile": profile,
            "skill_categories": skill_categories,
            "projects": projects,
            "experiences": experiences,
            "educations": educations,
            "certificates": certificates,
            "services": services,
            "testimonials": testimonials,
            "about_tags": about_tags,
            "form": form,
        },
    )


def submit_contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was submitted successfully.")
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True, "message": "Thanks! Your message has been received."})
            return redirect("home:index")
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    return redirect("home:index")
