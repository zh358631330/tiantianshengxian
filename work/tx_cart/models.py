from django.db import models
from tx_goods.models import *
from tx_user.models import *
# Create your models here.

class CartInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    user = models.ForeignKey(UserInfo)
    count = models.IntegerField()


