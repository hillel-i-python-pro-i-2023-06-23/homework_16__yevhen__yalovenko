from django.contrib.auth import get_user_model


def is_exist_admin():
    User = get_user_model()
    is_admin_exist = User.objects.get(is_superuser=True).exists()
    return is_admin_exist
