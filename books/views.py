from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, BannerSerializer
from .models import Book, Banner


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['GET'],detail=False,url_path="book/<name>/")
    def findBookByTitle(self,request,name):
        book = self.get_queryset().filter(title=name)
        if(len(book) == 0):
            return JsonResponse({'status':0,'message':'书名不存在'})
        else:
            return JsonResponse({'status':1,'message':'书名已存在'})


class BannerViewSet(ModelViewSet):
    # queryset = Banner.objects.filter(is_deleted=0)
    # print(queryset)
    # serializer_class = BannerSerializer

    @action(methods=['GET'],detail=False,url_path="books/banner/")
    def findBanners(self, request):
        queryset = Banner.objects.values().filter(is_deleted=0)
        # print(JsonResponse(list(queryset), safe=False))
        if (queryset != ''):
            return JsonResponse({'status': 200, 'data': list(queryset)},safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '链接有误'})





