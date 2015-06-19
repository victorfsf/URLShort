from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic.base import View
from shortener.forms import StoreURLForm
from shortener.models import URLBase
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from shortener import util


class StoreURL(FormView):
    template_name = 'index.html'
    form_class = StoreURLForm
    success_url = '/success/'
    
    def form_valid(self, form):
        try:
            url_check = URLBase.objects.get(link=form.instance.link)
            
        except URLBase.DoesNotExist:
            url_check = form.instance
            form.save()
        
        self.success_url = reverse('success') + '?link=' + util.to_base62(url_check.pk)
        
        return super(StoreURL, self).form_valid(form)

    def form_invalid(self, form):
        return super(StoreURL, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(StoreURL, self).get_context_data(**kwargs)
        return context
    

class GenerateURL(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super(GenerateURL, self).get_context_data(**kwargs)

        context['host'] = self.request.get_host()

        return context


class RedirectURL(View):

    def get(self, request, *args, **kwargs):
        short_id = self.kwargs['short_id']
        url_base = get_object_or_404(URLBase, pk=util.from_base62(short_id))
        return redirect(url_base.link)