from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    video = EmbedVideoField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    
    class  Meta:
        verbose_name_plural = "Videos"
        ordering = ('-id',)
        
    def  __str__(self):
        return  str(self.title) if  self.title  else  " "