from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ['title']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        # fields = "__all__"
        fields = ['carousel_id', 'carousel_url', 'redirect_url', 'carousel_rand']


class MallOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall_order
        fields = "__all__"
        # fields = ['order_no', 'total_price', 'pay_status', 'pay_type', 'order_status', 'extra_info', 'is_deleted',
        #           'create_time']
