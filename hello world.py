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
import os

DEBUG=os.environ.get('DEBUG','on') == on,
SECRET_KEY = os.environ.get('SECRET_KEY',os.urandom(32)),
ALLOWED_HOST=os.environ.get('ALLOWED_HOST','LOCALHOST','localhost').split(','),
settings.configure(
    #增加debug的设置选项，直接从系统环境变量中读取，使用os库
    #当debug为off时，需要借助allowed hosts变量的设置
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,
    ALLOWED_HOST = ALLOWED_HOST,
    ROOT_URLCONF = __name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

)
#导入设置文件，然后定义一个启动函数
#需要一个wsgi接口
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#其中sys.argv是一个参数导入函数
import sys
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)