from django.urls import path
from rest_framework.routers import DefaultRouter
from books import views

urlpatterns = [
    path('books/book/<name>/', views.BookViewSet.as_view({'get': 'findBookByTitle'})),
    path('books/banner/', views.BannerViewSet.as_view({'get': 'findBanners'})),
    path('books/order/', views.MallOrderViewSet.as_view({'get': 'findOrder'})),
    path('books/orderList/', views.OrderItemViewSet.as_view({'get': 'findOrderList'})),
    path('books/orderAddress/', views.OrderAddressViewSet.as_view({'get': 'findOrderAddress'})),
    path('books/userCollection/', views.UserCollectionViewSet.as_view({'get': 'findUserCollection'})),
    path('books/user/', views.UserViewSet),
    path('books/address/', views.AddressViewSet),
    path('books/token/', views.TokenViewSet),
    path('books/goods/', views.GoodsViewSet),
    path('books/category/', views.CategoryViewSet),
    path('books/cart/', views.CartViewSet),

    # 测试数据
    path('goods/home/', views.HomeViewSet.as_view({'get': 'getHome'})),
    path('goods/goodsDetails/', views.HomeViewSet.as_view({'get': 'getGoodsDetails'})),
    path('user/queryCollection/', views.UserViewSet.as_view({'get': 'getQueryCollection'})),
]


router = DefaultRouter()  # 括号不要忘了 ，不然执行不了
router.register(r"banner", views.BannerViewSet)
router.register(r"books", views.BookViewSet)
router.register(r"order", views.MallOrderViewSet)
router.register(r"orderList", views.OrderItemViewSet)
router.register(r"orderAddress", views.OrderAddressViewSet)
router.register(r"userCollection", views.UserCollectionViewSet)
router.register(r"user", views.UserViewSet)
router.register(r"address", views.AddressViewSet)
router.register(r"token", views.TokenViewSet)
router.register(r"goods", views.GoodsViewSet)
router.register(r"category", views.CategoryViewSet)
router.register(r"cart", views.CartViewSet)


urlpatterns += router.urls

print(router.urls)
