from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
import forgery_py
from random import seed, randint


# Create your models here.


class Article(models.Model):
    subject = models.CharField(max_length=30, unique=True)
    creator = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=30000, default='')
    photo = models.ImageField(upload_to="img/", null=True, blank=True)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(100)

    @classmethod
    def generate_data(cls):
        user = User.objects.first()
        for i in range(50):
            seed()
            subject = forgery_py.lorem_ipsum.title(randint(1, 5))
            message = paragraphe(randint(1, 5))
            url = f'https://picsum.photos/700/300?image={randint(1,1000)}'
            Article.objects.create(
                subject=subject,
                creator=user,
                message=message,
                photo=url
            )


def paragraphe(n):
    s = lambda: forgery_py.lorem_ipsum.sentence()
    p = lambda: ''.join([s() for k in range(randint(2, 40))])
    return ''.join(p() for j in range(5))


# def get_previsions(cls, date=datetime.today()):
#     query = cls.objects.filter(retrait=date, accepted=True, archived=False,
#                                cancelled=False, pickedup=False)
#     orders = {}
#     for i in query:
#         for k, v in i.get_order().items():
#             if k in orders:
#                 orders[k]['quantity'] += v['quantity']
#                 orders[k]['total'] = round(
#                     orders[k]['quantity'] * v['price'], 2)
#             else:
#                 orders[k] = v
#     articles = {k: v for k, v in sorted(orders.items(), key=lambda x: x)}
#     total_price = round(sum([orders[i]['total'] for i in orders]), 2)
#     total_quantity = sum([orders[i]['quantity'] for i in orders])
#     articles.update({
#         '': {
#             'quantity': total_quantity,
#             'price': '',
#             'total': total_price
#         }
#     })
#     return articles
