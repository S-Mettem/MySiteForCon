"""Main Map urls"""

# Includes
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


# Paths
app_name = 'MainMap'
urlpatterns = [
    path('', views.index, name='home'),
    path('map', views.map_view, name='map'),
    path('categories/', views.categories_view, name='categories'),
    path('categories/<slug:cat_name>/', views.category_view, name='category'),
    path('categories/<slug:cat_name>/<slug:sight_name>/', views.sight_view, name='sight'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)