from itertools import chain

from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, BannerSerializer, MallOrderSerializer, OrderItemSerializer, \
    OrderAddressSerializer, UserCollectionSerializer, UserSerializer, AddressSerializer, TokenSerializer, \
    GoodsSerializer, CategorySerializer, CartSerializer
from .models import Book, Banner, Mall_order, Order_item, Order_address, User_collection, User, Cart, Category, Goods, \
    Token, Address


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['GET'], detail=False, url_path="book/<name>/")
    def findBookByTitle(self, request, name):
        book = self.get_queryset().filter(title=name)
        if (len(book) == 0):
            return JsonResponse({'status': 0, 'message': '书名不存在'})
        else:
            return JsonResponse({'status': 1, 'message': '书名已存在'})


# 订单表
class MallOrderViewSet(ModelViewSet):
    queryset = Mall_order.objects.all()
    serializer_class = MallOrderSerializer


# 订单项表
class OrderItemViewSet(ModelViewSet):
    queryset = Order_item.objects.all()
    serializer_class = OrderItemSerializer


# 订单地址表
class OrderAddressViewSet(ModelViewSet):
    queryset = Order_address.objects.all()
    serializer_class = OrderAddressSerializer


# 首页广告图
class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.filter(is_deleted=0)
    # print(queryset)
    serializer_class = BannerSerializer

    @action(methods=['GET'], detail=False, url_path="books/banner/")
    def findBanners(self, request):
        queryset = Banner.objects.values().filter(is_deleted=0)
        # print(JsonResponse(list(queryset), safe=False))
        if (queryset != ''):
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})


# 收藏表
class UserCollectionViewSet(ModelViewSet):
    queryset = User_collection.objects.all()
    serializer_class = UserCollectionSerializer

    def queryCollection(self, request):
        user_id = request.data['user_id']
        order_id = request.data['order_id']
        print(order_id, user_id)
        is_collection = User_collection.objects.values().filter(user_id=user_id, order_id=order_id)
        if is_collection:
            return JsonResponse({'status': 200, 'data': 1}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': 0}, safe=False)


# 用户表
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(methods=['GET'], detail=False, url_path="user/queryCollection/")
    # def getQueryCollection(self, request):
    #     queryset = Goods.objects.values('is_collection')
    #
    #     if queryset != '':
    #         return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
    #     else:
    #         return JsonResponse({'status': 500, 'message': '链接有误'})


# 地址表
class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


# 用户token表
class TokenViewSet(ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


# 商品表
class GoodsViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


# 商品分类表
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 购物车表
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def addToShopCart(self, request):
        user_id = request.data['user_id']
        goods_id = request.data['goods_id']
        is_addtocart = Cart.objects.values().filter(user_id=user_id, goods_id=goods_id)
        if is_addtocart:
            return JsonResponse({'status': 200, 'data': 1}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': 0}, safe=False)


# 主页数据展示
class HomeViewSet(ModelViewSet):

    @action(methods=['POST'], detail=False, url_path="goods/home/")
    def getHome(self, request):
        queryset1 = Banner.objects.values().filter(is_deleted=0)
        queryset2 = Goods.objects.values()
        # 数量多于30的话则取前30
        if len(queryset2) > 30:
            queryset2 = queryset2[0:30]
        print(len(queryset2))
        result = {'mall_carouse': list(queryset1),
                  'goods_info': list(queryset2)}
        # print(request.data)
        if queryset1 != '' or queryset2 != '':
            return JsonResponse({'status': 200, 'data': result}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})

    def getGoodsDetails(self, request):
        goods_id = request.data['goods_id']
        goodsDetails = Goods.objects.values('goods_id', 'goods_name', 'goods_intro', 'goods_cover_img',
                                            'goods_detail_content', 'original_price', 'selling_price', 'stock_num',
                                            'goods_sell_status').filter(goods_id=goods_id)
        if goods_id != '':
            return JsonResponse({'status': 200, 'data': list(goodsDetails)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})


# 搜索展示
class SerchViewSet(ModelViewSet):
    def search(self, request):
        print(request.data)
        msg = request.data['msg']
        goods = Goods.objects.values().filter(goods_name__contains=msg)
        # 数量多于20的话则取前二十
        if len(goods) > 20:
            goods = goods[0:20]
        print(len(goods))
        if goods != '':
            return JsonResponse({'status': 200, 'data': list(goods)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})


# 注册
class RegisterViewSet(ModelViewSet):

    def register(self, request):
        print(request.data)
        name = request.data['name']
        pwd = request.data['pwd']
        user = User.objects.values().filter(login_name=name)
        # 判断用户是否已经存在
        if user:
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)
        # 存储到数据库中
        else:
            print(type(name), type(pwd))
            user = User.objects.create(login_name=name, user_pwd=pwd, nick_name='铁蛋', introduce='我是hhh')
            print("插入成功", user)
            # user.save()
            return JsonResponse({'status': 200, 'data': {'success': 1}}, safe=False)


# 登录
class LoginViewSet(ModelViewSet):

    def login(self, request):
        print(request.data)
        name = request.data['name']
        pwd = request.data['pwd']
        user = User.objects.values().filter(login_name=name, user_pwd=pwd)
        print(user[0])
        # 判断用户是否存在
        if user:
            print("账号密码正确")
            return JsonResponse({'status': 200, 'data': {'success': 1, 'user_id': user[0]['user_id']}}, safe=False)
        else:
            print("账号密码错误")
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)


# 用户信息
class UserInfoViewSet(ModelViewSet):

    def userInfo(self, request):
        print(request.data)
        user_id = request.data['user_id']
        userinfo = User.objects.values('user_id', 'login_name', 'user_pwd', 'nick_name', 'locked', 'introduce',
                                       'is_deleted', 'create_time').filter(user_id=user_id)
        print(userinfo)
        # 判断用户是否存在
        if userinfo:
            print("返回用户信息成功")
            return JsonResponse({'status': 200, 'data': userinfo[0]}, safe=False)
        else:
            print("返回用户信息失败")
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)


# 更新用户信息
class UpdateUserInfoViewSet(ModelViewSet):
    pass


# 用户收藏列表
class CollectionListViewSet(ModelViewSet):
    def collectionList(self, request):
        print(request.data)
        user_id = request.data['user_id']
        lists = User_collection.objects.values('order_id', 'is_deleted').filter(user_id=user_id)
        print(lists)
        # 判断是否存在收藏
        if lists:
            print("返回用户收藏成功")
            return JsonResponse({'status': 200, 'data': list(lists)}, safe=False)
        else:
            print("返回用户收藏失败")
            return JsonResponse({'status': 500, 'data': None}, safe=False)


class GoodsListViewSet(ModelViewSet):
    def goodsList(self, request):
        goodsList = Category.objects.values()
        #  print(goodsList)
        # 判断是否存在
        if goodsList:
            print("返回商品列表成功")
            return JsonResponse({'status': 200, 'data': list(goodsList)}, safe=False)
        else:
            print("返回商品列表失败")
            return JsonResponse({'status': 500, 'data': None}, safe=False)
        print()


# 查询购物车数据
class checkShopCartViewSet(ModelViewSet):
    def ShopCart(self, request):
        user_id = request.data['user_id']
        queryset = Cart.objects.values('cart_item_id', 'user_id', 'goods_id',
                                       'is_deleted').filter(user_id=user_id)
        if queryset:
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '数据有误'})


class AddressListViewSet(ModelViewSet):
    def AddressList(self, request):
        user_id = request.data['user_id']
        queryset = Address.objects.values('address_id', 'user_name', 'user_phone',
                                          'default_flag', 'province_name', 'city_name').filter(user_id=user_id)
        if queryset:
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '数据有误'})


class orderListViewSet(ModelViewSet):
    def getOrderList(self, request):
        user_id = request.data['user_id']

        queryset1 = Mall_order.objects.filter(user_id=user_id).values('order_no', 'total_price', 'order_status')
        queryset2 = Order_item.objects.filter(user_id=user_id).values('order_item_id', 'order_id', 'goods_name',
                                                                      'goods_name', 'goods_cover_img', 'selling_price',
                                                                      'goods_count')

        # items = chain(queryset1, queryset2)
        result = {'orderList': list(queryset1), 'orderItem': list(queryset2)}
        if result:
            # return JsonResponse({'status': 200, 'data': list(items)}, safe=False)
            return JsonResponse({'status': 200, 'data': result}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '数据有误'})


class editAddressViewSet(ModelViewSet):
    def editAddress(self, request):
        print(request.data)
        address_id = request.data['address_id']
        # user_id = request.data['user_id']
        user_name = request.data['user_name']
        user_phone = request.data['user_phone']
        default_flag = request.data['default_flag']
        province_name = request.data['province_name']
        city_name = request.data['city_name']
        region_name = request.data['region_name']
        detail_address = request.data['detail_address']
        print(address_id)
        queryset = Address.objects.values().filter(address_id=address_id)
        print(queryset)
        # print(address_id, user_name, user_phone, default_flag, province_name, city_name, region_name, detail_address)
        if queryset:
            address = Address.objects.filter(address_id=address_id).update(user_name=user_name, user_phone=user_phone,
                                                                           default_flag=default_flag,
                                                                           province_name=province_name,
                                                                           city_name=city_name, region_name=region_name,
                                                                           detail_address=detail_address)
            print("插入成功", address)
            print("插入成功")
            return JsonResponse({'status': 200, 'data': {'success': 1}}, safe=False)
        else:
            print("插入地址失败")
            return JsonResponse({'status': 500, 'message': '数据有误'})


class getdefAddressViewSet(ModelViewSet):
    def defAddress(self, request):
        user_id = request.data['user_id']
        queryset = Address.objects.filter(user_id=user_id, default_flag=1).values('province_name', 'city_name',
                                                                                  'region_name', 'detail_address')
        new_queryset = []
        for i in queryset:
            dic = {'province_name': i['province_name'], 'city_name': i['city_name'], 'country_name': i['region_name'],
                   'address_detail': i['detail_address']}
            new_queryset.append(dic)
        if queryset:
            return JsonResponse({'status': 200, 'data': list(new_queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '数据有误'})
