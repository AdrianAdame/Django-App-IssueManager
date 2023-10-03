from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("None", {"fields" : ("email", "role", "team")}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ("None", {"fields" : ("role", "team")}),
    )

    list_display = [
        "username",
        "email",
        "last_name",
        "first_name",
        "role",
        "team",
        "is_staff"
    ]


admin.site.register(CustomUser, CustomUserAdmin)
