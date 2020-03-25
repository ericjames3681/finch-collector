from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>/', views.records_detail, name='detail'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
    path('records/<int:record_id>/add_listening/', views.add_listening, name='add_listening'),
    path('records/<int:record_id>/assoc_dist/<int:distributor_id>/', views.assoc_dist, name='assoc_dist'),
    path('records/<int:record_id>/unassoc_dist/<int:distributor_id>/', views.unassoc_dist, name='unassoc_dist'),
    path('distributors/', views.DistributorList.as_view(), name='distributors_index'),
    path('distributors/<int:pk>/', views.DistributorDetail.as_view(), name='distributors_detail'),
    path('distributors/create/', views.DistributorCreate.as_view(), name='distributors_create'),
    path('distributors/<int:pk>/update/', views.DistributorUpdate.as_view(), name='distributors_update'),
    path('distributors/<int:pk>/delete/', views.DistributorDelete.as_view(), name='distributors_delete'),
]