from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

USER = get_user_model()

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

    def get_absolute_url(self):
        return reverse( 'news:story', kwargs={'pk': self.pk})


class Comment(models.Model):
    story = models.ForeignKey(NewsStory, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(USER, related_name="comments" ,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


