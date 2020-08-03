from django.contrib import admin
from .models import *

admin.AdminSite.site_header = '移动电商管理系统'
admin.AdminSite.site_title = '移动电商管理系统'


# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['carousel_id', 'carousel_url', 'redirect_url', 'carousel_rand', 'is_deleted', 'create_time']
#     fieldsets = [
#         ('轮播图URL', {'fields': ['carousel_url']}),
#         ('链接地址', {'fields': ['redirect_url']}),
#         ('轮播排序', {'fields': ['carousel_rand']}),
#         ('是否删除', {'fields': ['is_deleted']}),
#     ]
#     list_per_page = 10


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
    search_fields = ['title', 'price']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)

    # list_editable 设置默认可编辑字段
    list_editable = ['title']

    # fk_fields 设置显示外键字段
    fk_fields = ('publish_id',)


# 用户表
class UserAdmin(admin.ModelAdmin):
    list_display = ['login_name', 'user_pwd', 'nick_name', 'locked', 'introduce', 'is_deleted', 'create_time']
    fieldsets = [
        ('用户名', {'fields': ['login_name']}),
        ('用户密码', {'fields': ['user_pwd']}),
        ('昵称', {'fields': ['nick_name']}),
        ('个人简介', {'fields': ['introduce']}),
    ]
    list_per_page = 10


# 用户地址表
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'user_id', 'user_name', 'user_phone', 'default_flag',
                    'province_name', 'city_name', 'region_name', 'detail_address', 'create_time']
    fieldsets = [
        ('用户ID', {'fields': ['user_id']}),
        ('收货人姓名', {'fields': ['user_name']}),
        ('收货人电话', {'fields': ['user_phone']}),
        ('是否默认电话', {'fields': ['default_flag']}),
        ('省', {'fields': ['province_name']}),
        ('市', {'fields': ['city_name']}),
        ('地区', {'fields': ['region_name']}),
        ('详细地址', {'fields': ['detail_address']}),
    ]
    list_per_page = 10


# 用户token表
class TokenAdmin(admin.ModelAdmin):
    list_display = ['Token_id', 'user_id', 'token', 'update_time', 'expire_time']
    fieldsets = [
        ('用户ID', {'fields': ['user_id']}),
        ('Token', {'fields': ['token']}),
        ('过期时间', {'fields': ['expire_time']}),
    ]
    list_per_page = 10


# 商品信息表
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods_id', 'goods_name', 'goods_intro', 'goods_category', 'goods_cover_img',
                    'goods_carousel', 'goods_detail_content', 'original_price', 'selling_price', 'stock_num',
                    'tag', 'goods_sell_status', 'create_time']
    fieldsets = [
        ('商品名称', {'fields': ['goods_name']}),
        ('商品介绍', {'fields': ['goods_intro']}),
        ('商品分类', {'fields': ['goods_category']}),
        ('商品封面图', {'fields': ['goods_cover_img']}),
        ('商品滚屏', {'fields': ['goods_carousel']}),
        ('商品详情内容', {'fields': ['goods_detail_content']}),
        ('原价', {'fields': ['original_price']}),
        ('售价', {'fields': ['selling_price']}),
        ('库存数量', {'fields': ['stock_num']}),
        ('标签', {'fields': ['tag']}),
        ('商品销售状态', {'fields': ['goods_sell_status']}),
    ]
    list_per_page = 10


# 商品分类表
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_level', 'parent_id', 'category_name', 'category_rank',
                    'is_deleted', 'create_time']
    fieldsets = [
        ('分类级别', {'fields': ['category_level']}),
        ('父类ID', {'fields': ['parent_id']}),
        ('分类名称', {'fields': ['category_name']}),
        ('分类排名', {'fields': ['category_rank']})
    ]
    list_per_page = 10


# 购物车表
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_item_id', 'user_id', 'goods_id', 'goods_count',
                    'is_deleted', 'create_time', 'update_time']
    fieldsets = [
        ('用户ID', {'fields': ['user_id']}),
        ('商品ID', {'fields': ['goods_id']}),
        ('商品数量', {'fields': ['goods_count']})
    ]
    list_per_page = 10




# 订单表
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'order_no', 'total_price', 'pay_status', 'pay_type', 'pay_time',
                    'order_status', 'extra_info', 'is_deleted', 'create_time', 'update_time']
    fieldsets = [
        ('订单编码', {'fields': ['order_no']}),
        # ('用户ID', {'fields': ['user_id']}),
        ('总价', {'fields': ['total_price']}),
        ('支付状态', {'fields': ['pay_status']}),
        ('支付类型', {'fields': ['pay_type']}),
        ('订单状态', {'fields': ['order_status']}),
        ('备注', {'fields': ['extra_info']}),
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10


# 订单项表
class Order_itemAdmin(admin.ModelAdmin):
    list_display = ['order_item_id', 'goods_name', 'goods_cover_img',
                    'selling_price', 'goods_count', 'create_time']
    fieldsets = [
        ('商品名称', {'fields': ['goods_name']}),
        ('商品封面图', {'fields': ['goods_cover_img']}),
        ('销售价格', {'fields': ['selling_price']}),
        ('商品数量', {'fields': ['goods_count']}),
    ]
    list_per_page = 10


# 订单地址表
class Order_addressAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_phone', 'province_name',
                    'city_name', 'region_name', 'detail_address']
    fieldsets = [
        ('收货人姓名', {'fields': ['user_name']}),
        ('收货人电话', {'fields': ['user_phone']}),
        ('省', {'fields': ['province_name']}),
        ('市', {'fields': ['city_name']}),
        ('地区', {'fields': ['region_name']}),
        ('详细地址', {'fields': ['detail_address']}),
    ]
    list_per_page = 10


# 首页广告表
class BannerAdmin(admin.ModelAdmin):
    list_display = ['carousel_id', 'carousel_url', 'redirect_url',
                    'carousel_rand', 'is_deleted', 'create_time']
    fieldsets = [
        ('轮播图URL', {'fields': ['carousel_url']}),
        ('链接地址', {'fields': ['redirect_url']}),
        ('轮播排序', {'fields': ['carousel_rand']}),
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10


# 收藏表
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['collection_id', 'user_id',
                    'order_id', 'is_deleted']
    fieldsets = [
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10


admin.site.register(Book, BookAdmin)
# admin.site.register(Banner, BannerAdmin)

# zl
admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)

# zzx
admin.site.register(Mall_order, OrderAdmin)
admin.site.register(Order_item, Order_itemAdmin)
admin.site.register(Order_address, Order_addressAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(User_collection, CollectionAdmin)
