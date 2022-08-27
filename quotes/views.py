from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.views.generic import TemplateView

from quotes.utils.get_quotes import get_quote

# Create your views here.

class Imab5View(TemplateView):
    template_name = "imab5_qute.html"

    def get_context_data(self,*args, **kwargs):
        context = super(Imab5View, self).get_context_data(*args,**kwargs)

        context['imab5_quote'] = get_quote()

        return context


def get_imab5_quote(request):

    if request.method == 'GET':
        context = get_quote()

    return render(request, 'imab5_quote.html', {'imab5_quote': context})
