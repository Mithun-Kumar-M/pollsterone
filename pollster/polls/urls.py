from django.urls import path 

from . import views 

app_name = 'polls' 

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/', views.detail, name='detail'),           # For question detail (vote page)
    path('<int:question_id>/result/', views.result, name='result'), # For poll results page
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
