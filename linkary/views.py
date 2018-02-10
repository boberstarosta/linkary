from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from . import models


class LinkListView(ListView):
    model = models.Link
    template_name = 'linkary/index.html'
    ordering = ['-time_created']


class LinkDetailView(DetailView):
    model = models.Link


class BootstrapFormMixin(FormMixin):
    """Inherit from this class to create forms tagged for bootstrap."""
    def get_form(self, form_class=None):
        """Add bootstrap class "form-control" to each field before returning form."""
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form


class LinkCreateView(LoginRequiredMixin, BootstrapFormMixin, CreateView):
    model = models.Link
    fields = '__all__'


class LinkUpdateView(LoginRequiredMixin, BootstrapFormMixin, UpdateView):
    model = models.Link
    fields = '__all__'


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Link
    success_url = reverse_lazy('index')
