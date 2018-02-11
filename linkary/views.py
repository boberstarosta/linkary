from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, DeleteView, FormMixin
from . import forms, models


class LinkListView(ListView):
    model = models.Link
    template_name = 'linkary/index.html'
    ordering = ['-time_created']


class LinkDetailView(LoginRequiredMixin, DetailView):
    model = models.Link


class BootstrapFormMixin(FormMixin):
    """Inherit from this class to create forms tagged for bootstrap."""
    def get_form(self, form_class=None):
        """Add bootstrap class "form-control" to each field before returning form."""
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form


class LinkCreateView(LoginRequiredMixin, BootstrapFormMixin, View):
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


class LinkUpdateView(LoginRequiredMixin, BootstrapFormMixin, UpdateView):
    model = models.Link
    fields = '__all__'


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Link
    success_url = reverse_lazy('index')


class UserRegistrationView(View):
    form_class = forms.UserRegistrationForm
    template_name = 'linkary/registration_form.html'

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
