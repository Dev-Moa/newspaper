from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View

from articles.forms import CommentForm
from .models import article
from django.views.generic import ListView,DetailView,FormView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin

# Create your views here.

class ArticleListView(ListView):
    model = article
    template_name = "artciles/article_list.html"


class CommentGet(DetailView):
    model = article
    template_name = "articles/article_detail.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
class CommentPost(SingleObjectMixin, FormView):
    model = article
    form_class = CommentForm
    template_name = "article_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})

class ArticleDetailView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class articleCreateView(LoginRequiredMixin,CreateView):
    model = article
    fields = ['title','body']
    template_name = 'articles/article_create.html'
    # knowing each author 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class articleEditView(LoginRequiredMixin,UpdateView):
    model = article
    template_name = "articles/article_edit.html"
    fields = ['title','body']
class articleDeleteView(LoginRequiredMixin,DeleteView):
    model = article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('articles')
