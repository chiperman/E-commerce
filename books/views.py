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

    @action(methods=['GET'], detail=False, url_path="user/queryCollection/")
    def getQueryCollection(self, request):
        queryset = Goods.objects.values('is_collection')

        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})



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


class HomeViewSet(ModelViewSet):
    queryset1 = Banner.objects.filter(is_deleted=0)
    queryset2 = Goods.objects.filter(goods_sell_status=1)

    @action(methods=['GET'], detail=False, url_path="goods/home/")
    def getHome(self, request):
        queryset1 = Banner.objects.values().filter(is_deleted=0)
        queryset2 = Goods.objects.values().filter(goods_sell_status=1)

        result = {'mall_carouse': list(queryset1),
                  'goods_info': list(queryset2)}
        # print(result)
        # print(JsonResponse(list(queryset), safe=False))
        if queryset1 != '' or queryset2 != '':
            return JsonResponse({'status': 200, 'data': result}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})

    @action(methods=['GET'], detail=False, url_path="goods/goodsDetails/")
    def getGoodsDetails(self, request):
        queryset = Goods.objects.values('goods_id', 'goods_name', 'goods_intro', 'goods_category', 'goods_cover_img',
                                        'goods_detail_content', 'original_price', 'selling_price', 'stock_num', 'tag',
                                        'goods_sell_status')

        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})



