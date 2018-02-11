from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, View
from django.views.generic.edit import UpdateView, DeleteView, FormMixin
from . import forms, models


class LinkListView(ListView):
    model = models.Link
    template_name = 'linkary/index.html'
    ordering = ['-time_created']


class UserRegistrationView(View):
    form_class = forms.UserRegistrationForm
    template_name = 'registration/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            user.save()

            # Returns user object if credentials are correct
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class LinkDetailView(LoginRequiredMixin, DetailView):
    model = models.Link


class LinkCreateView(LoginRequiredMixin, View):
    form_class = forms.LinkModelForm
    template_name = 'linkary/link_create_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            link = form.save(commit=False)
            link.author = request.user
            link.save()
            return redirect('link_detail', pk=link.pk)

        return render(request, self.template_name, {'form': form})


class LinkUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Link
    form_class = forms.LinkModelForm
    template_name = 'linkary/link_update_form.html'


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Link
    success_url = reverse_lazy('index')


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    ordering = ['name']


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'linkary/category_create_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = 'linkary/category_update_form.html'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    success_url = reverse_lazy('category_list')
