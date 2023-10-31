from django.db import models

class Category (models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_open_for_part_time_work =models.BooleanField(default=False)

    is_open_for_full_time_work =models.BooleanField(default=False)
    is_open_for_gigs =models.BooleanField(default=False)
    is_open_for_internships =models.BooleanField(default=False)
    image=models.ImageField(upload_to='item_images',blank=True, null=True)
    video = models.FileField(upload_to='item_videos', blank=True, null=True)


    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='project_images', blank=True, null=True)
    demo_link = models.URLField(max_length=200)
    demo_video = models.FileField(upload_to='project_videos', blank=True, null=True)

    def __str__(self):
        return self.title