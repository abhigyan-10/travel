from django.contrib.auth import get_user_model

User = get_user_model()

def create_admin():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "yourpassword")
        return "Superuser created!"
    return "Superuser already exists!"
