from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """Reusable contact form for the portfolio site."""

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your phone"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Tell me more about your idea"}),
        }
