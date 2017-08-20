import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import *

logger = logging.getLogger('blog.views')


# Create your views here.

def global_setting(request):
    return {
        'SITE_URL': 'http://localhost:8000/',
        'SITE_NAME': '鸟嘌呤的个人博客',
        'SITE_DESC': '专注Python开发，欢迎和大家交流',
        'WEIBO_SINA': 'http://weibo.sina.com/yopoing',
        'WEIBO_TENCENT': 'http://weibo.qq.com/yopoing',
        'PRO_RSS': 'http://ww2w.baidu.com',
        'PRO_EMAIL': 'yopoing@vip.qq.com'
    }


def index(request):
    try:
        # file = open('aaa.txt', 'r')
        # 分类信息获取
        category_list = Category.objects.all()[:1]
        # 广告数据

        # 最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 10)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, PageNotAnInteger, InvalidPage):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)

    return render(request, 'index.html', locals())
