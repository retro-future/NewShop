from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """Задача отправки email-уведомлений при успешном оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. ' \
              'Your order id id {}.'.format(order.first_name, order_id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    print('order_created function')
    return mail_sent
