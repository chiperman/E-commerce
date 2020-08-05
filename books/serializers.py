from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ['title']


# 订单表
class MallOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall_order
        # fields = "__all__"
        fields = ['order_no', 'total_price', 'pay_status', 'pay_type', 'order_status', 'extra_info', 'is_deleted',
                  'create_time']


# 订单项表
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = "__all__"


# 订单地址表
class OrderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_address
        fields = "__all__"


# 首页广告表
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        # fields = "__all__"
        fields = ['carousel_id', 'carousel_url', 'redirect_url', 'carousel_rand']


# 收藏表
class UserCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_collection
        fields = "__all__"
