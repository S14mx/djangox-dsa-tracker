from django.urls import path


from .views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionDeleteView, QuestionUpdateView

urlpatterns = [
    path('', QuestionListView.as_view(), name='list_question'),
    path('<int:pk>', QuestionDetailView.as_view(), name='detail_question'),
    path('create', QuestionCreateView.as_view(), name='create_question'),
    path('<int:pk>/update', QuestionUpdateView.as_view(), name='update_question'),
    path('<int:pk>/delete', QuestionDeleteView.as_view(), name='delete_question'),
]
