
from django.contrib import admin
from django.urls import path
from task1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', sign_up),
    path('', index),
    # path('platform/', platform),
    path('games/', games),
    path('cart/', cart)

]
