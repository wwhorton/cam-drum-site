from django.views import generic
from .models import Topic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'cam_drum_site/index.html'
    model = Topic

    def get_context_data(self, *, object_list=None, **kwargs):
        nav_items = Topic.objects.all()
        context = super().get_context_data(**kwargs)
        context['nav_items'] = nav_items
        return context


class DetailView(generic.DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        nav_items = Topic.objects.all()
        context = super().get_context_data(**kwargs)
        context['nav_items'] = nav_items
        return context
