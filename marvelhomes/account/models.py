from django.db import models

# Create your models here.
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news_photos/', blank=True)
    description = models.TextField()
    updated_time = models.TimeField()
    updated_date = models.DateField()
    photo_count = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.photo and self.photo_count < 15:
            self.photo_count += 1
        super().save(*args, **kwargs)