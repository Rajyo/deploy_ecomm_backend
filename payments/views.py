from django.shortcuts import redirect
import stripe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decouple import config

# Create your views here.
stripe.pk_key = config('STRIPE_PUBLIC_KEY')
stripe.api_key = config('STRIPE_PRIVATE_KEY')

# @api_view(['POST'])
# def test_payment(request):
#     test_payment_intent = stripe.PaymentIntent.create(
#     amount=1000, currency='pln', 
#     payment_method_types=['card'],
#     receipt_email='test@example.com')
#     return Response(status=status.HTTP_200_OK, data=test_payment_intent)

# def save_stripe_info(request):
#     data = request.data
#     email = data['email']
#     payment_method_id = data['payment_method_id']
    
#     # creating customer
#     customer = stripe.Customer.create(
#       email=email, payment_method=payment_method_id)
     
#     return Response(status=status.HTTP_200_OK, 
#       data={
#         'message': 'Success', 
#         'data': {'customer_id': customer.id}   
#       })

# @api_view(['POST'])
# def save_stripe_info(request):
#   data = request.data
#   email = data['email']
#   payment_method_id = data['payment_method_id']
#   extra_msg = '' # add new variable to response message  # checking if customer with provided email already exists
#   customer_data = stripe.Customer.list(email=email).data   
 
#   # if the array is empty it means the email has not been used yet  
#   if len(customer_data) == 0:
#     # creating customer
#     customer = stripe.Customer.create(
#     email=email, payment_method=payment_method_id)  
#   else:
#     customer = customer_data[0]
#     extra_msg = "Customer already existed."  
    
#   return Response(status=status.HTTP_200_OK, 
#     data={'message': 'Success', 'data': {
#       'customer_id': customer.id, 'extra_msg': extra_msg}
#    })


# class StripeCheckoutView(APIView):
#     def post(self, request):
#         try:
#             checkout_session = stripe.checkout.Session.create(
#                 line_items=[
#                     {
#                         'price': '{{PRICE_ID}}',
#                         'quantity': 1,
#                     },
#                 ],
#                 payment_method_types=['card',],
#                 mode='payment',
#                 success_url= 'http://localhost:3000/?success=true',
#                 cancel_url= 'http://localhost:3000/?canceled=true',
#             )

#             return redirect(checkout_session.url)
#         except:
#             return Response(
#                 {'error': 'Something went wrong when creating stripe checkout session'},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )
        

# @api_view(['POST'])
# def test_payment(request):
#     test_payment_intent = stripe.PaymentIntent.create(
#     amount=1000, currency='pln', 
#     payment_method_types=['card'],
#     receipt_email='test@example.com')
#     return Response(status=status.HTTP_200_OK, data=test_payment_intent)

# @api_view(['POST'])
# def save_stripe_info(request):
#   data = request.data
#   email = data['email']
#   payment_method_id = data['payment_method_id']
#   extra_msg = '' # add new variable to response message  # checking if customer with provided email already exists
#   customer_data = stripe.Customer.list(email=email).data   
 
#   # if the array is empty it means the email has not been used yet  
#   if len(customer_data) == 0:
#     # creating customer
#     customer = stripe.Customer.create(
#     email=email, payment_method=payment_method_id)  
#   else:
#     customer = customer_data[0]
#     extra_msg = "Customer already existed."  


#   stripe.PaymentIntent.create(
#     customer=customer, 
#     payment_method=payment_method_id,  
#     currency='usd', # you can provide any currency you want
#     amount=55500, # I modified amount to distinguish payments
#     # confirmation_method = "manual",
#     automatic_payment_methods={"enabled": True},
#   )
  
#   print(customer, payment_method_id)

#   return Response(status=status.HTTP_200_OK, 
#     data={'message': 'Success', 'data': {
#       'customer_id': customer.id, 'extra_msg': extra_msg}
#    })

@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000,
        currency='pln',
        payment_method_types=['card'],
        receipt_email='test@example.com',
    )

    return Response(status=status.HTTP_200_OK, data=test_payment_intent)


# @api_view(['POST'])
# def confirm_payment_intent(request):
#     data = request.data
#     payment_intent_id = data['payment_intent_id']

#     stripe.PaymentIntent.confirm(payment_intent_id)

#     return Response(status=status.HTTP_200_OK, data={"message": "Success"})


@api_view(['POST'])
def save_stripe_info(request):
    data = request.data
    email = data['email']
    description = data['description']
    amount = data['amount']
    name = data['name']
    line1 = data['line1']
    line2 = data['line2']
    postal_code = data['postal_code']
    city = data['city']
    state = data['state']
    country = data['country']
    payment_method_id = data['payment_method_id']
    extra_msg = ''
    # checking if customer with provided email already exists
    customer_data = stripe.Customer.list(email=email).data
    print(customer_data)

    if len(customer_data) == 0:
        # creating customer
        customer = stripe.Customer.create(
            name=name,
            address={
              "line1": line1,
              "line2":line2,
              "postal_code": postal_code,
              "city": city,
              "state": state,
              "country": country,
            },
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
    else:
        customer = customer_data[0]
        extra_msg = "Customer already existed."
    
    print('customer',customer)

    # creating paymentIntent

    payment = stripe.PaymentIntent.create(customer=customer,
                                payment_method=payment_method_id,
                                currency='inr', amount=amount*100,
                                description=description,
                                confirm=True)
    print('payment',payment)
    stripe.PaymentIntent.confirm(payment.id)
    print(payment.next_action.use_stripe_sdk.stripe_js)

    return Response(status=status.HTTP_200_OK, data={'message': 'Success', 'data': {'customer': customer,'payment':payment,
                                                                                    'extra_msg': extra_msg, 'payment_url':payment.next_action.use_stripe_sdk.stripe_js}})
