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
]


router = DefaultRouter()  # 括号不要忘了 ，不然执行不了
router.register(r"banner", views.BannerViewSet)
router.register(r"books", views.BookViewSet)
router.register(r"order", views.MallOrderViewSet)
router.register(r"orderList", views.OrderItemViewSet)
router.register(r"orderAddress", views.OrderAddressViewSet)
router.register(r"userCollection", views.UserCollectionViewSet)

urlpatterns += router.urls

print(router.urls)
