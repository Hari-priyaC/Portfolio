def site_settings(request):
    """Provide shared settings to all templates."""
    return {
        "site_name": "Haripriya C",
        "site_title": "Python Backend Developer",
        "site_email": "haripriya@example.com",
    }
