from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets_second/', views.snippet_list_second),
    path('snippets_second/<int:pk>/', views.snippet_detail_second),
    path('snippets_third/', views.SnippetList.as_view()),
    path('snippets_third/<int:pk>/', views.SnipetDetail.as_view()),
    path('snippets_fourth/', views.SnippetList_fourth.as_view()),
path('snippets_fifth/', views.SnipetList_fifth.as_view()),
path('snippets_fifth/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)