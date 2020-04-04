from django.urls import path

from .views import index, by_rubric, BbCreateView, BbDetailView, BbEditView, BbDeleteView
#app_name = 'bboard'
urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name = 'detail'),
    path('izmenit/<int:pk>/', BbEditView.as_view(), name = 'update'),
    path('udalit/<int:pk>/', BbDeleteView.as_view(), name = 'ddd'),
    path('', index, name='index'),
]
