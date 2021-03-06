from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.http import is_safe_url
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.conf import settings

from .forms import CompanyForm, CompanyInfoForm, SortForm
from .models import Company,CompanyInfo

from datetime import date

# Create your views here.

def index(request):
    return redirect('company:list', sort='next')

@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
    model = Company

    def get_queryset(self):
        key = self.kwargs['sort']
        companies = Company.objects.filter(user=self.request.user)
        companies = companies.order_by(key)
        return companies

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)  #テンプレートに渡すコンテキストに 「user_count」 という変数を追加
            context['date'] = date.today()
            context['form'] = SortForm
            return context

def sort(request):
    if request.method == "POST":
        s = request.POST.get('key')
        return redirect('company:list', sort=s)
    else:
        return redirect('company:list', sort='next')

@method_decorator(login_required, name='dispatch')
class CompanyCreateView(CreateView):
    form_class = CompanyForm
    template_name = 'company/company_create.html'
    success_url = reverse_lazy('company:index')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(CompanyCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm

    def get_success_url(self):
        return original_url(self)

@require_POST
def delete(request,pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return redirect_to_origin(request)

def info(request,pk):
    try:
        info = CompanyInfo.objects.get(company_id=pk)
        return redirect('company:detailinfo', pk=info.pk)
    except:
        return redirect('company:createinfo', pk=pk)

@method_decorator(login_required, name='dispatch')
class CompanyInfoDetailView(DetailView):
    model = CompanyInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meta_fields = CompanyInfo._meta.get_fields()
        dic = {}
        for field in meta_fields:
            if field.name != 'id' and field.name != 'user':
                exec('dic[field.verbose_name]=context["object"].{}'.format(field.name))
        context['info'] = dic
        return context


@method_decorator(login_required, name='dispatch')
class CompanyInfoCreateView(CreateView):
    form_class = CompanyInfoForm
    template_name = 'company/companyinfo_create.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.company_id = self.kwargs['pk']
        return super(CompanyInfoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.get(id=self.kwargs['pk'])
        context['name'] = company.name
        return context

    def get_success_url(self):
        info = CompanyInfo.objects.get(company_id=self.kwargs['pk'])
        return reverse_lazy('company:detailinfo', kwargs={'pk': info.pk})

@method_decorator(login_required, name='dispatch')
class CompanyInfoUpdateView(UpdateView):
    model = CompanyInfo
    form_class = CompanyInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companyinfo = CompanyInfo.objects.get(id=self.kwargs['pk'])
        context['name'] = companyinfo.company.name
        return context

    def get_success_url(self):
        return original_url(self)

@require_POST
def deleteinfo(request,pk):
    company = get_object_or_404(CompanyInfo, pk=pk)
    company.delete()
    return redirect('company:index')

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

