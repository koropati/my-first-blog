from django.contrib import admin
from .models import Post, Jurnal, Data
# Register your models here.
admin.site.register(Post)
admin.site.register(Jurnal)
admin.site.register(Data)