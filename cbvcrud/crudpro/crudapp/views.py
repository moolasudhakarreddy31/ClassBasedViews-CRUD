from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from crudapp.models import Company
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
# from django.urls import reverse
# Create your views here.

class CompanyListView(ListView):
    model=Company


class CompanyDetailview(DetailView):
    model=Company
    # template_name='crudapp/company_details.html'

class CompanyCreateview(CreateView):
    model=Company
    fields=('name','ceo','location')

class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo','location')
    slug_field = 'company_slug'

    # def get_queryset(self):
    # # def get_object(self, queryset=None):
    #     slug = self.kwargs.get('slug')
    #     return Company.objects.get(slug=slug)

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('company_list')