from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from main_app.models import Reply, Advert


def replies_by_advert(request, advert_pk):
    advert = Advert.objects.get(id=advert_pk)
    adv_replies = Reply.objects.filter(advert=advert_pk).order_by('created_reply')
    context = {'advert': advert, 'adv_replies': adv_replies}
    return render(request, 'protect/replies.html', context)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/profile.html'
    model = Advert

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_announcers'] = not self.request.user.groups.filter(name='announcers').exists()
        context['adverts'] = Advert.objects.filter(announcer=self.request.user.id).order_by('-created')
        context['replies'] = Reply.objects.filter(user=self.request.user).order_by('-created_reply')
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'protect/profile.html'
    form_class = UserForm
    success_url = '/'


def delete_reply(request, advert_pk, reply_pk):
    reply = Reply.objects.get(id=reply_pk)
    reply.delete()
    return redirect(f'/{advert_pk}/')


def take_reply(request, advert_pk, reply_pk):
    reply = Reply.objects.get(id=reply_pk)
    reply.save()
    send_mail(
        subject='Your reply is taken',
        message=f'Hi! Your reply from {reply.created_reply} is taken.',
        from_email='Freezyyyyy@yandex.ru',
        recipient_list=[request.user.email]
    )
    return redirect(f'/{advert_pk}/')

