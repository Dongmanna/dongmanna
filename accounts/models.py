# accounts/models.py
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from main.models import Post

class Profile(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank =True)
    my_image = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)
	rating = models.FloatField(default=0, blank=True)
	post_attended = models.ManyToManyField(Profile, blank=True, related_name='post_attended_profile')

	def __str__(self):
        return self.nickname