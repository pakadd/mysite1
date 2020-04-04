from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Bb, Rubric
from .forms import BbForm

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bbs, 3)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.page(page_num)
    context = {'bbs': page.object_list, 'rubrics':rubrics, 'page': page}
    #context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    rubrucs = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    bbs = Bb.objects.filter(rubric=rubric_id)
    context = {'bbs': bbs, 'rubrics':rubrucs, 'current_rubric':current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbDeleteView(DeleteView):
    model = Bb
    ##form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbDetailView(DetailView):
    model = Bb
    template_name = 'bboard/detal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
