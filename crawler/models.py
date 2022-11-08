from datetime import timezone
from django.db import models

class CrawledArticle(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="عنوان")
    text = models.TextField(null=True, blank=True, verbose_name="متن")
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)


    def __str__(self):
        return str(self.title)

    
    class Meta:
        verbose_name = "مقاله اینترنتی"
        verbose_name_plural = "مقاله های اینترنتی"
