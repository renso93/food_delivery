from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users" 
    label = "users"
    verbose_name = "Gestion des utilisateurs"
    icon_name = "person"
    hide_in_dashboard = False
    hide_in_menu = False
    order_index = 10
    required_permissions = [
        "users.view_user",
        "users.add_user",
        "users.change_user",
        "users.delete_user",
    ]
    