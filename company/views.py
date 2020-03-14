from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .forms import CompanyForm
from .models import Company

# Create your views here.

@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
    model = Company
    template_name = 'menu/list.html'
    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CompanyCreateView(CreateView):
    form_class = CompanyForm
    template_name = 'form/create.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(CompanyCreateView, self).form_valid(form)

    def get_success_url(self):
        try:
            return original_url(self)
        except:
            return reverse_lazy('accounts:index', kwargs={'pk': self.request.user.id})

@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'form/update.html'

    def get_success_url(self):
        try:
            return original_url(self)
        except:
            return reverse_lazy('accounts:index', kwargs={'pk': self.request.user.id})

@method_decorator(login_required, name='dispatch')
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'form/delete.html'

    def get_success_url(self):
        try:
            return original_url(self)
        except:
            return reverse_lazy('accounts:index', kwargs={'pk': self.request.user.id})



def redirect_to_origin(request):
    redirect_to = request.GET.get('next')
    url_is_safe = is_safe_url(
        url=redirect_to,
        allowed_hosts=settings.ALLOWED_HOSTS,
        require_https=request.is_secure(),
    )
    if url_is_safe and redirect_to:
        return redirect(redirect_to)

def original_url(self):
    url = self.request.GET.get('next')
    url_is_safe = is_safe_url(
        url=url,
        allowed_hosts=settings.ALLOWED_HOSTS,
        require_https=self.request.is_secure(),
    )
    if url_is_safe and url:
        return url

