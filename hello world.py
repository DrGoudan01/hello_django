#__author__ = 'li'
# -*- coding:utf-8 -*-
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello world')
#定义一个输出，这是view的内容
from django.conf.urls import url
urlpatterns = (
    url(r'^$',index),
)
#定义了url的规则
from django.conf import settings
settings.configure(
    DEBUG=True,
    SECRET_KEY = 'thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

)
#导入设置文件，然后定义一个启动函数
#其中sys.argv是一个参数导入函数
import sys
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)