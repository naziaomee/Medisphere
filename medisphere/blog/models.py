from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
