from django.db import models

# Create your models here.
class dailyNews(models.Model):
    newsTitle= models.CharField(max_length=200)
    newsDetails= models.TextField()
    image = models.ImageField(upload_to='news_images')

    def __str__(self):
        return "%s" %(self.newsTitle)

        class Meta:
            db_table = "news"
