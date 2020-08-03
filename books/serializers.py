from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        #fields = ['title']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        #fields = "__all__"
        fields = ['carousel_id','carousel_url','redirect_url','carousel_rand']
