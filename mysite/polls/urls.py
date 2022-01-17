from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename='question')
# router.register(r'choices', views.ChoiceViewSet, basename='choice')
# app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]

## amend the URLconf
app_name = 'polls'
urlpatterns = [
    path('polls/', views.IndexView.as_view(), name='index'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    # for api
    path('api/', include(router.urls)),
]