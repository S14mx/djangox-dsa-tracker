from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CompletedQuestion
from django.urls import reverse_lazy


class QuestionListView(ListView):
    template_name = 'dsa_tracker/question_list.html'
    model = CompletedQuestion


class QuestionDetailView(DetailView):
    template_name = 'dsa_tracker/question_detail.html'
    model = CompletedQuestion


class QuestionCreateView(CreateView):
    template_name = 'dsa_tracker/question_create.html'
    model = CompletedQuestion
    fields = ['name', 'notes', 'time_to_complete', 'completed_by',]
    success_url = reverse_lazy('list_question')


class QuestionUpdateView(UpdateView):
    template_name = 'dsa_tracker/question_update.html'
    model = CompletedQuestion
    fields = ['name', 'notes', 'time_to_complete',]


class QuestionDeleteView(DeleteView):
    template_name = 'dsa_tracker/question_delete.html'
    model = CompletedQuestion
    success_url = reverse_lazy('list_question')
