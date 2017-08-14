import logging
from django.shortcuts import render
from django.conf import settings

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
        pass
    except Exception as e:
        logger.error(e)

    return render(request, 'index.html', locals())
