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


# 用户表
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# 地址表
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


# Token表
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"


# 商品表
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"
        # fields = ['goods_id']


# 商品分类表
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# 购物车表
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

