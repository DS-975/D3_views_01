from django.contrib import admin
from django.urls import path, include # include <- Для работы приложения Flatpages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),  # <- Для работы приложения Flatpages
]