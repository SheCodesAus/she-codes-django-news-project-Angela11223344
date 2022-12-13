from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    # class Meta:
    #     ordering = ['-pub_date']
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()   
    image_url = models.URLField(blank=True) 
    #blank=True means it's ok not to have an image


