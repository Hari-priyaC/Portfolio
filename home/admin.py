from django.contrib import admin

from .models import (
    Certificate,
    ContactMessage,
    Education,
    Experience,
    Profile,
    Project,
    Skill,
    SkillCategory,
)

admin.site.register(Profile)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(ContactMessage)
