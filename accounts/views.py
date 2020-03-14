from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date

class IndexView(TemplateView):
    template_name = 'menu/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  #テンプレートに渡すコンテキストに 「user_count」 という変数を追加
        context['date'] = date.today()
        return context

