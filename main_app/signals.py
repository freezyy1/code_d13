from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import mail_managers, mail_admins, send_mail
from .models import Reply, Advert


@receiver(post_save, sender=Advert)
def notify_managers_post(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.adv_name} {instance.created.strftime("%d %m %Y")}'
    else:
        subject = f'Advert changed for {instance.adv_name} {instance.created.strftime("%d %m %Y")}'

    send_mail(
        subject=subject,
        message=instance.content[:20] + '...',
        from_email='Freezyyyyy@yandex.ru',
        recipient_list=[instance.announcer.user.email, ]
    )

    mail_admins(
        subject=subject,
        message=instance.content[:30] + '...',
    )


@receiver(post_save, sender=Reply)
def notify_managers_post(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.text} {instance.created_reply.strftime("%d %m %Y")}'
    else:
        subject = f'Reply accepted for {instance.text} {instance.created_reply.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.text,
    )

    send_mail(
        subject=subject,
        message=instance.text,
        from_email='Freezyyyyy@yandex.ru',
        recipient_list=[instance.user.email, instance.advert.announcer.user.email, ]
    )

    mail_admins(
        subject=subject,
        message=instance.text,
    )


@receiver(post_delete, sender=Reply)
def notify_managers_post_canceled(sender, instance, **kwargs):
    subject = f'{instance.text} has canceled his reply!'

    mail_managers(
        subject=subject,
        message=f'Canceled reply for {instance.created_reply.strftime("%d %m %Y")}',
    )

    print(subject)

