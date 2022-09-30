from django.contrib import admin
from .models import Video
from embed_video.admin import AdminVideoMixin

@admin.register(Video)
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	list_display = ('id','title', 'text', 'video')