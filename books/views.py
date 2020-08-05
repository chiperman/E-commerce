from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, BannerSerializer, MallOrderSerializer, OrderItemSerializer, \
    OrderAddressSerializer, UserCollectionSerializer
from .models import Book, Banner, Mall_order, Order_item, Order_address, User_collection


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

class ddd:
    pass
# 收藏表
class UserCollectionViewSet(ModelViewSet):
    queryset = User_collection.objects.all()
    serializer_class = UserCollectionSerializer
