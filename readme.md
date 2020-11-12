# Django 项目搭建

## 一、安装环境

pip3 install django

## 二、创建项目

django-admin startproject my_django

查看my_django目录下结构

```
my_django/
    manage.py
    my_django/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

manage.py —— 项目启动

settings.py —— 项目配置

urls.py —— 项目的URL映射

wsgi.py、asgi.py —— WSGI部署、ASGI部署


# 三、接口开发

参考my_django目录下 view.py 与 urls.py

# 四、项目启动

### 启动方式一:

启动命令
```
python manage.py runserver 127.0.0.1:8000
```
参考示例代码：访问 localhost:8000/hello

### 启动方式二:

IDE中右键manage.py, 选择```Edis ‘manage’...```

弹出框中 Parameters项填上 ```runserver 127.0.0.1:8000```

保存后，可选择运行或debug执行manage启动项目

# 五、ORM操作

###### 数据库连接:

1.修改setting的‘DATABASES’

###### 建立数据模型:

2.创建user模型，执行命令 ```python manage.py startapp user```。执行完当前目录会增加一个user文件夹

3./user/models.py中编写模型类

4.执行以下操作，生成数据库表
```
python manage.py makemigrations user 
python manage.py migrate
```

###### 执行sql操作:

5.orm常规操作，参考user/views.py
