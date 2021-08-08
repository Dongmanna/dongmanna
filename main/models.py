# main/models.py
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import Profile
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill



class Post(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE, related_name='author_post')
    category = models.CharField(max_length=20,
        choices=(
            ('오프라인', 'Offline'),
            ('온라인', 'Online'),
            ('배달음식', 'Delivery'),
        ))
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField(default='')
    # region = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    # 일단은 모집인원 최소 1명 최대 10명으로 설정해놓음
    limit = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    link = models.URLField(max_length=300, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    members = models.ManyToManyField(Profile, blank=True, related_name='members_post')
    image = ProcessedImageField(
    		blank = True,
        	upload_to = 'post/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    
    		)
    def __str__(self):
        return self.title

# class Image(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE) 
#     image = models.ImageField(upload_to='images/', blank=True, null=True)

