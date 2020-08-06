from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, BannerSerializer, MallOrderSerializer, OrderItemSerializer, \
    OrderAddressSerializer, UserCollectionSerializer, UserSerializer, AddressSerializer, TokenSerializer, \
    GoodsSerializer, CategorySerializer
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


# 用户表
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
    serializer_class = CategorySerializer


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
        # 判断用户是否存在
        if user:
            print("账号密码正确")
            return JsonResponse({'status': 200, 'data': {'success': 1}}, safe=False)
        else:
            print("账号密码错误")
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)
        print()


# 用户信息
class UserInfoViewSet(ModelViewSet):
    def userInfo(self, request):
        print(request.data)
        name = request.data['name']
        pwd = request.data['pwd']
        user = User.objects.values().filter(login_name=name, user_pwd=pwd)
        # 判断用户是否存在
        if user:
            print("账号密码正确")
            return JsonResponse({'status': 200, 'data': {'success': 1}}, safe=False)
        else:
            print("账号密码错误")
            return JsonResponse({'status': 500, 'data': {'success': 0}}, safe=False)
        print()