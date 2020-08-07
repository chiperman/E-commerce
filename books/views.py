import random
import uuid
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


# 添加购物车表
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def addToShopCart(self, request):
        user_id = request.data['userId']
        goods_id = request.data['goodsId']
        Cart.objects.create(user_id=user_id, goods_id=goods_id, goods_count="1", update_time='2003-04-01')
        # is_addtocart = Cart.objects.values().filter(user_id=user_id, goods_id=goods_id,
        return JsonResponse({'status': 200, 'data': {"success": 1}}, safe=False)
        # return JsonResponse({'status': 500, 'data': {"success": 0}}, safe=False)


# 主页数据展示
class HomeViewSet(ModelViewSet):

    @action(methods=['POST'], detail=False, url_path="goods/home/")
    def getHome(self, request):
        queryset1 = Banner.objects.values().filter(is_deleted=0)
        queryset2 = Goods.objects.values()
        queryset3 = []
        # 数量多于30的话则取前30
        if len(queryset2) > 30:
            for i in range(30):
                j = random.randint(0, len(queryset2)-1)
                queryset3.append(queryset2[j])
        # print(len(queryset2))
        result = {'mall_carousel': list(queryset1),
                  'goods_info': list(queryset3)}
        # print(request.data)
        if queryset1 != '' or queryset2 != '':
            return JsonResponse({'status': 200, 'data': result}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})

    def getGoodsDetails(self, request):
        goods_id = request.data['goodsId']
        print(goods_id)
        goodsDetails = Goods.objects.values('goods_id', 'goods_name', 'goods_intro', 'goods_cover_img',
                                            'goods_detail_content', 'original_price', 'selling_price', 'stock_num',
                                            'goods_sell_status').filter(goods_id=goods_id).first()
        print(goodsDetails)
        if goods_id != '':
            return JsonResponse({'status': 200, 'data': {"goods_info": goodsDetails}}, safe=False)
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
        name = request.data['username']
        pwd = request.data['password']
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
        name = request.data['username']
        pwd = request.data['password']
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
        user_id = request.data['userId']
        lists = User_collection.objects.values('order_id', 'is_deleted').filter(user_id=user_id, is_deleted=0)
        print(lists)
        new_lists = []
        for i in lists:
            # print(i)
            if i['is_deleted'] == 1:
                i['is_deleted'] = True
            else:
                i['is_deleted'] =False
            dic = {'goods_id': i['order_id'], 'is_deleted': i['is_deleted']}
            list2 = Goods.objects.values().filter(goods_id=i['order_id']).first()
            dic.update(list2)
            new_lists.append(dic)

        # 判断是否存在收藏
        if lists:
            print("返回用户收藏成功")
            return JsonResponse({'status': 200, 'data': {"collect_Info":list(new_lists)}}, safe=False)
        else:
            print("返回用户收藏失败")
            return JsonResponse({'status': 500, 'data': None}, safe=False)


# 商品模块,分类商品列表
class GoodsListViewSet(ModelViewSet):
    def goodsList(self, request):
        goodsList = Category.objects.values()
        #  print(goodsList)
        # 判断是否存在
        if goodsList:
            print("返回商品列表成功")
            return JsonResponse({'status': 200, 'data': {"goods_info": list(goodsList)}}, safe=False)
        else:
            print("返回商品列表失败")
            return JsonResponse({'status': 500, 'data': None}, safe=False)
        print()


# 查询购物车数据
class checkShopCartViewSet(ModelViewSet):
    def ShopCart(self, request):
        print(request.data)
        user_id = request.data['userId']
        carts = []
        queryset = Cart.objects.values('cart_item_id', 'user_id', 'goods_id',
                                       'is_deleted', 'goods_count').filter(user_id=user_id, is_deleted=0)
        for i in queryset:
            # print(i)
            queryset2 = Goods.objects.values('goods_name', 'goods_cover_img', 'selling_price').filter(
                goods_id=i['goods_id']).first()
            dic = {"cart_item_id": i["cart_item_id"],
                   "user_id": i["user_id"],
                   "goods_id": i["goods_id"],
                   "is_deleted": i["is_deleted"],
                   "goods_name": queryset2["goods_name"],
                   "goods_cover_img": queryset2["goods_cover_img"],
                   "selling_price": queryset2["selling_price"],
                   "goods_count": i["goods_count"]}
            carts.append(dic)
        if queryset:
            return JsonResponse({'status': 200, 'data': {"shopping_cart": carts}}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': None})


# 地址列表
class AddressListViewSet(ModelViewSet):
    def AddressList(self, request):
        user_id = request.data['userId']
        queryset = Address.objects.values('address_id', 'user_name', 'user_phone',
                                          'default_flag', 'province_name', 'city_name').filter(user_id=user_id)
        if queryset:
            return JsonResponse({'status': 200, 'data': {"address_info": list(queryset)}}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': None})


# 获取订单列表
class orderListViewSet(ModelViewSet):
    def getOrderList(self, request):
        user_id = request.data['userId']

        queryset1 = Mall_order.objects.filter(user_id=user_id).values('order_no', 'total_price', 'order_status',
                                                                      'order_id')
        # queryset2 = Order_item.objects.filter(user_id=user_id).values('order_item_id', 'goods_name','order_id'
        #                                                               'goods_cover_img', 'selling_price',
        #                                                               'goods_count')

        result = []
        for i in queryset1:
            print(i)
            result2 = []
            queryset2 = Order_item.objects.filter(order_id=i['order_id']).values('order_item_id', 'goods_name',
                                                                                 'goods_cover_img', 'selling_price',
                                                                                 'goods_count')
            for j in queryset2:
                dic = {'order_no': i['order_no'], 'order_item_id': j['order_item_id'],
                       'goods_name': j['goods_name'], 'goods_cover_img': j['goods_cover_img'],
                       'selling_price': j['selling_price'], 'goods_count': j['goods_count'],
                       'total_price': i['total_price'], 'order_status': i['order_status']}
                result2.append(dic)
            result.append(result2)
        print(result)

        if queryset1:
            return JsonResponse({'status': 200, 'data': result}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '数据有误'})


# 编辑收货地址
class editAddressViewSet(ModelViewSet):
    def editAddress(self, request):
        print(request.data)
        address_id = request.data['addressId']
        user_id = request.data['userId']
        user_name = request.data['userName']
        user_phone = request.data['userPhone']
        default_flag = request.data['defaltFlag']
        if default_flag:
            default_flag = 1
        else:
            default_flag = 0
        province_name = request.data['provinceName']
        city_name = request.data['cityName']
        region_name = request.data['countryName']
        detail_address = "123456"
        print(address_id)
        # queryset = Address.objects.values().filter(address_id=address_id)
        # print(queryset)
        # print(address_id, user_name, user_phone, default_flag, province_name, city_name, region_name, detail_address)
        if address_id != "":
            address = Address.objects.filter(address_id=address_id).update(user_name=user_name, user_phone=user_phone,
                                                                           default_flag=default_flag,
                                                                           province_name=province_name,
                                                                           city_name=city_name, region_name=region_name,
                                                                           detail_address=detail_address)
            print("修改地址成功", address)
            return JsonResponse({'status': 200, 'data': {'success': 1}}, safe=False)
        else:
            Address.objects.create(user_id=user_id, user_name=user_name, user_phone=user_phone,
                                   default_flag=default_flag,
                                   province_name=province_name,
                                   city_name=city_name, region_name=region_name,
                                   detail_address=detail_address)
            print("插入新的地址")
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)


# 默认地址
class getdefAddressViewSet(ModelViewSet):
    def defAddress(self, request):
        user_id = request.data['user_id']
        queryset = Address.objects.filter(user_id=user_id, default_flag=1).values('province_name', 'city_name',
                                                                                  'region_name', 'detail_address')
        new_queryset = []
        for i in queryset:
            print(i)
            dic = {'province_name': i['province_name'], 'city_name': i['city_name'], 'country_name': i['region_name'],
                   'address_detail': i['detail_address']}
            new_queryset.append(dic)
        if queryset:
            return JsonResponse({'status': 200, 'data': list(new_queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '数据有误'})


# 删除购物车商品
class delCartGoodsViewSet(ModelViewSet):
    def delCartGoods(self, request):
        user_id = request.data['userId']
        cart_item_id = request.data['cartItemId']
        # queryset = Cart.objects.filter(cart_item_id=cart_item_id).values('is_deleted')
        Cart.objects.filter(cart_item_id=cart_item_id).update(is_deleted=1)
        queryset = Cart.objects.filter(cart_item_id=cart_item_id).values('is_deleted')
        for i in queryset:
            if i['is_deleted'] == 1:
                return JsonResponse({'status': 200, 'data': {'success': 1}}, safe=False)
            else:
                return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)


# 商品收藏、取消
class isCollectionsViewSet(ModelViewSet):
    def is_collection(self, request):
        user_id = request.data['userId']
        goods_id = request.data['goodsId']
        is_deleted = request.data['isDeleted']
        queryset = User_collection.objects.filter(user_id=user_id, order_id=goods_id)
        if queryset:
            User_collection.objects.filter(user_id=user_id, order_id=goods_id).update(is_deleted=is_deleted)
            print("改变收藏状态")
            return JsonResponse({'status': 200, 'data': {'is_collection': is_deleted}}, safe=False)
        else:
            User_collection.objects.create(user_id=user_id, order_id=goods_id)
            print("添加收藏")
            return JsonResponse({'status': 500, 'data': {'is_collection': is_deleted}},safe=False)


# 删除收货地址
class delAddressViewSet(ModelViewSet):
    def delAddress(self, requset):
        address_id = requset.data['address_id']
        queryset = Address.objects.filter(address_id=address_id).values()
        print(list(queryset))
        if queryset:
            delAddressAction = Address.objects.get(address_id=address_id).delete()
            return JsonResponse({'status': 200, 'data': {'delAddress': 1}}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '数据有误'})


# 提交订单
class submitOrderViewSet(ModelViewSet):
    def submitOrder(self, request):
        order_id = uuid.uuid4()
        order_no = uuid.uuid4()
        user_id = request.data['userId']
        total_price = request.data['totalPrice']
        pay_status = request.data['payStatus']
        pay_type = request.data['payType']
        goodsInfo = request.data['goodsInfo']

        queryset = Mall_order.objects.create(order_id=order_id, order_no=order_no, user_id=user_id,
                                             total_price=total_price, pay_status=pay_status, pay_type=pay_type)
        for i in goodsInfo:
            print(i)
            Order_item.objects.create(order_id=order_id,
                                      goods_id=i['goods_id'],
                                      user_id=i['user_id'],
                                      goods_name=i['goods_name'],
                                      goods_cover_img=i['goods_cover_img'],
                                      selling_price=i['selling_price'],
                                      goods_count=i['goods_count'])
        if queryset:
            return JsonResponse({'status': 200, 'data': {'success': 1}}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)


class CategorySearchViewSet(ModelViewSet):
    def categorySearch(self, request):
        print(request.data)
        category_name = request.data['categoryName']
        goods = Goods.objects.values('goods_name','goods_cover_img').filter(goods_name__contains=category_name)
        good = []
        for i in range(len(goods)):
            j = random.randint(0, len(goods) - 1)
            good.append(goods[j])
        if goods:
            print("返回分类正确")
            return JsonResponse({'status': 200, 'data': {"goods_info":list(goods)}}, safe=False)
        else:
            print("返回分类错误")
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)