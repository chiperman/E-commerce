from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField(auto_now_add=True)

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'book'



class Banner(models.Model):
    carousel_id = models.IntegerField(auto_created=True,primary_key=True)
    carousel_url = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=100)
    carousel_rand = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
            db_table = 'mall_carousel'


class mall_order(models.Model):
    order_id = models.IntegerField(auto_created=True, primary_key=True)
    order_no = models.CharField(max_length=100, unique=True)
    total_price = models.FloatField()
    pay_status = models.IntegerField(default=0)
    pay_type = models.CharField(max_length=100)
    pay_time = models.DateTimeField(auto_now_add=True)
    order_status = models.IntegerField(default=0)
    extra_info = models.CharField(max_length=100)
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = 'mall_order'

class order_item(models.Model):
    order_item_id = models.IntegerField(auto_created=True, primary_key=True)
    goods_name = models.CharField(max_length=100)
    goods_cover_img = models.CharField(max_length=100)
    selling_price = models.FloatField()
    goods_count = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
            db_table = 'order_item'

class order_address(models.Model):
    user_name = models.CharField(max_length=32)
    user_phone = models.CharField(max_length=32)
    province_name = models.CharField(max_length=32)
    city_name = models.CharField(max_length=32)
    region_name = models.CharField(max_length=32)
    detail_address = models.CharField(max_length=100)

    class Meta:
            db_table = 'order_address'

class user_collection(models.Model):
    collection_id = models.IntegerField(auto_created=True, primary_key=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
            db_table = 'user_collection'