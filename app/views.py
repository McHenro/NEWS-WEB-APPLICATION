from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage
from .models import News
from django.views.generic.list import ListView
from .serializers import NewsSerializer
from rest_framework import generics


def object_list():
    obj_list = []
    url_top_news = f"https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    item_id = requests.get(url_top_news).json()
    for item in item_id[:100]:
        url_news_items = (
            f"https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty"
        )
        response = requests.get(url_news_items).json()
        obj_list.append(response)
    print(obj_list)
    return obj_list


def index(request):
    item_list = object_list()
    paginator = Paginator(item_list, 20)
    page_num = request.GET.get("page", 1)
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)

    context = {"data": page, "item_list": item_list}
    return render(request, "app/index.html", context)


def search(request):
    value = request.GET.get("search")
    queryset = News.objects.filter(title__contains=value)

    context = {
        "queryset": queryset,
    }
    return render(request, "app/index.html", context)


class SearchView(ListView):
    model = News
    template_name = "app/search.html"
    context_object_name = "all_search_results"

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get("search")
        if query:
            post_result = News.objects.filter(title__contains=query)
            result = post_result
        else:
            result = None
        return result


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
