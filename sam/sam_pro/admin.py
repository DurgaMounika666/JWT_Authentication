from django.contrib import admin

# Register your models here.
from .models import Login

class Login_pro(admin.ModelAdmin):
    list_display = ('id','username','email','password','mobile',)


admin.site.register(Login, Login_pro)