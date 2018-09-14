from django.contrib import admin
# from django.urls import path
from django.conf.urls import include, url  # import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # r = regular exp.
    url(r'^movie1/', include('movie1.urls')),  # movie1 ke urls ko check karega or action krta hai
]
# sbse phle browser url check krega EX= 127.0.0.1:8000/admin = False
# fr second url check krega or movie1 = True me jayga fr movie1 ke url ko check krega
#mayank sharma
#akash birla
