from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
import logging
from .filters import AdvertFilter
from .forms import AdvertForm, ReplyForm
from .models import Advert, Reply


logger = logging.getLogger(__name__)

logger.debug("Hello! I'm debug in your app. Enjoy:)")
logger.info("Hello! I'm info in your app. Enjoy:)")
logger.warning("Hello! I'm warning in your app. Enjoy:)")
logger.error("Hello! I'm error in your app. Enjoy:)")
logger.critical("Hello! I'm critical in your app. Enjoy:)")


class AdvertListView(ListView):
    model = Advert
    template_name = 'adverts/adverts.html'
    context_object_name = 'adverts'
    queryset = Advert.objects.order_by('-created')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AdvertFilter(self.request.GET, queryset=self.get_queryset())

        return context


class AdvertDetailView(DetailView, FormView):
    template_name = 'adverts/advert.html'
    model = Advert
    form_class = ReplyForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advert = kwargs.get("object")
        new_reply = None
        context['advert'] = advert
        context['new_reply'] = new_reply
        context['reply_form'] = self.form_class()
        return context


class AdvertCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('adverts.add_post',)
    template_name = 'adverts/advert_create.html'
    form_class = AdvertForm
    success_url = '/adverts/'


class AdvertUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('adverts.change_post',)
    template_name = 'adverts/advert_create.html'
    form_class = AdvertForm
    success_url = '/adverts/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advert.objects.get(pk=id)


class AdvertDeleteView(DeleteView):
    template_name = 'adverts/advert_delete.html'
    queryset = Advert.objects.all()
    success_url = '/adverts/'


class ReplyListView(ListView):
    model = Reply
    template_name = 'adverts/advert.html'
    context_object_name = 'replies'
    queryset = Reply.objects.order_by('-created_reply')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ReplyDetailView(FormView):
    template_name = 'adverts/advert.html'
    form_class = ReplyForm
    success_url = "/"

    def form_valid(self, form) -> HttpResponse:
        print(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advert = get_object_or_404(Advert, id=id)
        replies = Advert.replies.all()
        new_reply = None
        context['advert'] = advert
        context['replies'] = replies
        context['new_reply'] = new_reply

        return context


class ReplyCreateView(CreateView):
    template_name = 'adverts/advert.html'
    form_class = ReplyForm
    success_url = '/adverts/'


class ReplyUpdateView(UpdateView):
    template_name = 'adverts/advert.html'
    form_class = ReplyForm


class ReplyDeleteView(DeleteView):
    template_name = 'protect/reply_delete.html'
    queryset = Reply.objects.all()
    success_url = '/'


