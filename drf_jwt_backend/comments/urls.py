from django.urls import path
from comments import views



urlpatterns = [
    path('all/', views.get_all_comments),
    path('', views.user_comments),
    path('<int:pk>', views.user_comments),
    path('<int:pk>/all/replies',views.get_all_replies),
    path('<int:pk>/replies', views.user_reply),
    
]
