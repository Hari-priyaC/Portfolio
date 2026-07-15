from django.core.management.base import BaseCommand

from home.models import (
    Certificate,
    Education,
    Experience,
    Profile,
    Project,
    Skill,
    SkillCategory,
)


class Command(BaseCommand):
    help = "Seed the portfolio with demo content"

    def handle(self, *args, **options):
        Profile.objects.all().delete()
        SkillCategory.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certificate.objects.all().delete()

        profile = Profile.objects.create(
            name="Haripriya C",
            title="Python Backend Developer",
            subtitle="Crafting high-performance web applications and APIs",
            bio="I design secure, scalable backend systems with Django, FastAPI, and cloud-native architecture.",
            years_experience=4,
            projects_completed=25,
            apis_delivered=100,
            technologies_used=15,
            email="haripriya@example.com",
            phone="+91 98765 43210",
            location="Bengaluru, India",
            github_url="https://github.com",
            linkedin_url="https://linkedin.com",
            instagram_url="https://instagram.com",
            resume_url="/static/resume/haripriya_resume.txt",
        )

        categories = [
            ("Frontend", "frontend"),
            ("Backend", "backend"),
            ("Database", "database"),
            ("Tools", "tools"),
        ]
        for name, slug in categories:
            SkillCategory.objects.create(name=name, slug=slug)

        skills = [
            ("Frontend", "HTML", 92),
            ("Frontend", "CSS", 90),
            ("Frontend", "Bootstrap", 95),
            ("Frontend", "JavaScript", 88),
            ("Frontend", "jQuery", 84),
            ("Backend", "Python", 96),
            ("Backend", "Django", 95),
            ("Backend", "DRF", 93),
            ("Backend", "FastAPI", 90),
            ("Database", "PostgreSQL", 90),
            ("Database", "MySQL", 84),
            ("Database", "SQLite", 88),
            ("Tools", "Git", 92),
            ("Tools", "Docker", 90),
            ("Tools", "Redis", 88),
            ("Tools", "Celery", 86),
            ("Tools", "Kafka", 84),
            ("Tools", "Nginx", 82),
            ("Tools", "Gunicorn", 80),
            ("Tools", "Linux", 85),
        ]
        for category_name, title, level in skills:
            category = SkillCategory.objects.get(name=category_name)
            Skill.objects.create(profile=profile, category=category, title=title, level=level)

        projects = [
            {
                "title": "Smart Task Board",
                "description": "A collaborative task management platform with workflow automation and business rules.",
                "category": "Django",
                "technologies": "Django, Bootstrap, jQuery, AJAX",
                "github_url": "https://github.com",
                "live_url": "https://example.com",
                "image": "images/project-smart-task.svg",
            },
            {
                "title": "Audio Transcription System",
                "description": "An AI-powered transcription app for audio uploads, annotation, and translation workflows.",
                "category": "AI",
                "technologies": "Django, Whisper AI, FFmpeg, WaveSurfer.js",
                "github_url": "https://github.com",
                "live_url": "https://example.com",
                "image": "images/project-audio.svg",
            },
            {
                "title": "Banking Management System",
                "description": "Role-based banking operations with secure APIs and token authentication.",
                "category": "Django",
                "technologies": "Django, REST API, Celery, Redis",
                "github_url": "https://github.com",
                "live_url": "https://example.com",
                "image": "images/project-banking.svg",
            },
            {
                "title": "Kafka Notification System",
                "description": "An event-driven notification pipeline with producer-consumer patterns and message filtering.",
                "category": "FastAPI",
                "technologies": "Kafka, Redis, Celery, Django",
                "github_url": "https://github.com",
                "live_url": "https://example.com",
                "image": "images/project-kafka.svg",
            },
        ]
        for item in projects:
            Project.objects.create(profile=profile, **item)

        experiences = [
            {
                "role": "Senior Backend Developer",
                "company": "Northstar Labs",
                "location": "Bengaluru",
                "start_date": "2022-01-01",
                "end_date": None,
                "description": "Built secure APIs, event-driven systems, and cloud deployments.",
                "current": True,
            },
            {
                "role": "Python Developer",
                "company": "BrightStack",
                "location": "Hyderabad",
                "start_date": "2020-06-01",
                "end_date": "2021-12-31",
                "description": "Delivered Django applications and integrations for enterprise clients.",
                "current": False,
            },
        ]
        for item in experiences:
            Experience.objects.create(profile=profile, **item)

        Education.objects.create(
            profile=profile,
            school="University of Technology",
            degree="B.Tech in Computer Science",
            years="2016-2020",
            description="Focused on software engineering, distributed systems, and databases.",
        )

        Certificate.objects.bulk_create(
            [
                Certificate(profile=profile, title="Python Programming", issuer="Coursera", issued_on="2023-05-01"),
                Certificate(profile=profile, title="Django Web Development", issuer="Udemy", issued_on="2024-01-15"),
                Certificate(profile=profile, title="REST API Design", issuer="Pluralsight", issued_on="2024-06-20"),
                Certificate(profile=profile, title="Docker Essentials", issuer="LinkedIn Learning", issued_on="2025-02-01"),
            ]
        )

        self.stdout.write(self.style.SUCCESS("Portfolio demo data created successfully."))
