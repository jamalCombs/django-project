from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from recommend_project.mixins import NextUrlMixin, RequestFormAttachMixin
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from .forms import LoginForm

class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'
    default_next = '/'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)
