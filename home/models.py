from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=220, blank=True)
    bio = models.TextField()
    years_experience = models.PositiveIntegerField(default=4)
    projects_completed = models.PositiveIntegerField(default=25)
    apis_delivered = models.PositiveIntegerField(default=100)
    technologies_used = models.PositiveIntegerField(default=15)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=120, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    about_image = models.ImageField(upload_to="about/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name="skills", on_delete=models.CASCADE)
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    level = models.PositiveIntegerField(default=85)

    def __str__(self):
        return f"{self.title} ({self.level}%)"


class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=80, default="Django")
    technologies = models.CharField(max_length=220)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name="experiences", on_delete=models.CASCADE)
    role = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name="educations", on_delete=models.CASCADE)
    school = models.CharField(max_length=120)
    degree = models.CharField(max_length=160)
    years = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.school


class Certificate(models.Model):
    profile = models.ForeignKey(Profile, related_name="certificates", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    issuer = models.CharField(max_length=120)
    issued_on = models.DateField()

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
