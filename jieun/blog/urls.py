from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    #예시: blog/
    path('', views.PostLV.as_view(), name='index'),
    #예시: blog/post
    path('post/', views.PostLV.as_view(), name='post_list'),
    #예시: blog/post/슬러그-슬러그-슬러그
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    #예시: blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    #예시: blog/archive/2022
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    #예시: blog/archive/2022/9월
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    #예시: blog/archive/2022/9월/16
    path('archive/<int:year>/<str:month>/<int:day>', views.PostDAV.as_view(), name='post_day_archive'),
    #예시: blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_toady_archive'),
    #예시: blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    #예시: blog/tag/tagname
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    path('search/', views.SearchFV.as_view(), name='post_search'),

    path('add/', views.PostCreateView.as_view(), name='add'),
    path('change/', views.PostChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),

    path('search/', views.SearchFV.as_view(), name='search'),

    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('category/change/', views.CategoryChangeLV.as_view(), name='category_change'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('site/', views.SiteView.as_view(), name='site'),

    path('site/add/', views.SiteCreateView.as_view(), name='site_add'),
    path('site/change/', views.SiteChangeLV.as_view(), name='site_change'),
    path('site/<int:pk>/update/', views.SiteUpdateView.as_view(), name='site_update'),
    path('site/<int:pk>/delete/', views.SiteDeleteView.as_view(), name='site_delete'),

]