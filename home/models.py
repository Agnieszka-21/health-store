from django.db import models


class Carousel(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    banner_img1 = models.ImageField(null=True, blank=True)
    name_banner_img1 = models.CharField(max_length=254, default='Banner image number one')
    banner_img2 = models.ImageField(null=True, blank=True)
    name_banner_img2 = models.CharField(max_length=254, default='Banner image number two')
    banner_img3 = models.ImageField(null=True, blank=True)
    name_banner_img3 = models.CharField(max_length=254, default='Banner image number three')
    banner_img4 = models.ImageField(null=True, blank=True)
    name_banner_img4 = models.CharField(max_length=254, default='Banner image number four')
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    display = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
