from django.contrib import admin
from .models import  Posts
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserChangeForm,CustomUserCreationForm

#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser



admin.site.register(Posts)
# admin.site.register(CustomUser)

