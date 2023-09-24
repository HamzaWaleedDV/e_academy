from django.views.decorators.csrf import csrf_exempt
import stripe
import academy.settings as settings
from django.http import HttpResponse
from .models import Transaction, Order, Course


@csrf_exempt
def stripe_webhook(request):
    print('Stripe webhook')
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
        )
    except ValueError as e:
        print('Invalid payload')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print('Invalid signature')
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        print('payment_intent.succeeded')
        transaction_id = payment_intent.metadata.transaction
        make_order(transaction_id)
        print(payment_intent.metadata)
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event['type']))
    return HttpResponse(status=200)



def make_order(transaction_id):
    transaction = Transaction.objects.get(pk=transaction_id)
    order = Order.objects.create(transaction=transaction)
    course = Course.objects.filter(pk=transaction.course_id)

    order.orderproduct_set.create(
        course_id=transaction.course_id,
        price=transaction.course.price
    )