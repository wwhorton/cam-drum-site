from django.views import generic
from .models import Article


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'cam_drum_site/index.html'
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DetailView(generic.DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
