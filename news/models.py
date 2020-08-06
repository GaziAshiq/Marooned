from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Tag(models.Model):
    tag_name = models.CharField(max_length=64, unique=True)
    tag_slug = models.SlugField(max_length=64, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse("news:tag-detail", kwargs={"slug": str(self.tag_slug)})


class News(models.Model):
    title = models.CharField(max_length=192, unique=True)
    slug = models.SlugField(max_length=192, unique=True)
    cover_photo = models.ImageField(upload_to='news', blank=True, null=True)
    summary = models.CharField(max_length=280)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    tags = models.ManyToManyField(Tag, blank=True, related_name='post_tag')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:post", kwargs={"slug": str(self.slug)})

# class Comment(models.Model):
#     post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=96)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['created_on']
#
#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)
