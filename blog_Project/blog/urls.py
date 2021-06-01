from django.urls import path

from blog import views

urlpatterns = [
    path('', views.post_list_view, name='post_list_view'),
    path('tag/?<slug:tag_slug>/', views.post_list_view, name='post_list_by_tag_name'),
    # path('',views.PostListView.as_view(),name='PostListView'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail'),
    path('<int:id>/share/', views.mail_send_view, name='mail_send_view'),
    #path('mail/', views.mail_send_view, name='mail_send_view'),
]