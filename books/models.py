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