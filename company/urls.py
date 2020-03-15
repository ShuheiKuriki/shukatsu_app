from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:sort>', views.CompanyListView.as_view(), name='list'),
    path('sort', views.sort, name='sort'),
    path('create', views.CompanyCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.CompanyUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.CompanyDeleteView.as_view(), name='delete'),
    path('<int:pk>', views.CompanyInfoDetailView.as_view(), name='detailinfo'),
    path('<int:pk>/info', views.info, name='info'),
    path('<int:pk>/createinfo', views.CompanyInfoCreateView.as_view(), name='createinfo'),
    path('<int:pk>/updateinfo', views.CompanyInfoUpdateView.as_view(), name='updateinfo'),
    path('<int:pk>/deleteinfo', views.CompanyInfoDeleteView.as_view(), name='deleteinfo'),


]