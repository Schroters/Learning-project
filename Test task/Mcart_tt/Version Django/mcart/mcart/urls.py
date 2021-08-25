from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('currency.urls'))      # Получается при переходе на главную страницу, будет вызываться файл urls.
]
