from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormMixin
from . import models


class LinkListView(ListView):
    model = models.Link
    template_name = 'linkary/index.html'


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


class LinkCreateView(BootstrapFormMixin, CreateView):
    model = models.Link
    fields = '__all__'
