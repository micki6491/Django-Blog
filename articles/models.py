from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
import forgery_py
from random import seed, randint
from markdown import markdown
import math
import feedparser
# Create your models here.

from django.db import models


# class FeedModule(models.Model):
#     title = models.CharField(max_length=20, default='default')
#     message = models.TextField(max_length=1000, default='default')
#     author = models.CharField(max_length=15, default='default')
#     date = models.DateTimeField(auto_now_add=False)
#
#     @classmethod
#     def update_feed(cls):
#         d = feedparser.parse('https://github.com/micki6491/Django-Blog/commits/master.atom')
#         a = d.entries[0]
#         date = d.feed.updated
#         title = a.title
#         message = a.content
#         if FeedModule.objects.count() == 0:
#             f = FeedModule.objects.create(title=title, message=message, date=date)
#             f.save()
#         else:
#             f = FeedModule.objects.last()
#             f.delete()
#             f = FeedModule.objects.create(title=title, message=message, date=date)
#             f.save()
#         return f


class Publication(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    subject = models.CharField(max_length=30, unique=True)
    creator = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=30000, default='')
    photo = models.ImageField(upload_to="img/", null=True, blank=True)
    publication = models.ForeignKey(Publication, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ('created_at',)

    @classmethod
    def generate_data(cls):
        user = User.objects.first()
        publications = Publication.objects.all()
        for i in range(25):
            seed()
            publication = publications[randint(0, publications.count() - 1)]
            subject = forgery_py.lorem_ipsum.title(randint(1, 5))
            message = paragraphe(randint(1, 5))
            url = f'https://picsum.photos/950/450?image={randint(1,1000)}'
            Article.objects.create(
                publication=publication,
                subject=subject,
                creator=user,
                message=message,
                photo=url
            )

    def get_message_as_markdown(self):
        return mark_safe((markdown(self.message, safe_mode='escape')))


def paragraphe(n):
    s = lambda: forgery_py.lorem_ipsum.sentence()
    p = lambda: ''.join([s() for k in range(randint(2, 40))])
    return '\n\n'.join(p() for j in range(5))
