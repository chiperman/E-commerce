from django.urls import path
from rest_framework.routers import DefaultRouter
from books import views

urlpatterns = [
    path('books/book/<name>/',views.BookViewSet.as_view({'get':'findBookByTitle'})),
    path('books/banner/',views.BannerViewSet.as_view({'get':'findBanners'})),

]

router=DefaultRouter()  # 括号不要忘了 ，不然执行不了
# router.register(r"books/banner/",views.BannerViewSet)
router.register(r"books",views.BookViewSet)


urlpatterns+=router.urls


print(router.urls)