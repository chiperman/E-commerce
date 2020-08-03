
from django.contrib import admin
from .models import *


admin.AdminSite.site_header = '移动电商管理系统'
admin.AdminSite.site_title = '移动电商管理系统'


class BannerAdmin(admin.ModelAdmin):
    list_display = ['carousel_id', 'carousel_url', 'redirect_url','carousel_rand','is_deleted','create_time']
    fieldsets = [
        ('轮播图URL', {'fields': ['carousel_url']}),
        ('链接地址', {'fields': ['redirect_url']}),
        ('轮播排序', {'fields': ['carousel_rand']}),
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']

    # 这个fields字段作用域model的添加页面，显示哪些字段可以用于输入内容，不在列表中的数据，默认添加页面就不在显示了。
    # fields = ['p_name']

    # fields属性和fieldsets属性不能同时使用。因为都作用于添加页面。
    fieldsets = [
        ('书名', {'fields': ['title']}),
        ('价格', {'fields': ['price']}),
        ('出版日期', {'fields': ['pub_date']}),
    ]

    # 针对人员列表页的一个属性配置，在列表页的右侧会出现一个过滤器，可以根据人员的年龄和性别对列表页的人员进行筛选。
    list_filter = ['price', 'pub_date']

    # # 在人员的列表页顶部会出现一个搜索框。只能根据search_fields内部定义的字段值进行搜索。
    search_fields = ['title','price']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)

    # list_editable 设置默认可编辑字段
    list_editable = ['title']

    # fk_fields 设置显示外键字段
    fk_fields = ('publish_id',)



admin.site.register(Book,BookAdmin)
admin.site.register(Banner,BannerAdmin)