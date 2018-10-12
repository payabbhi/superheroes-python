# import the Flask class from the flask module
from flask import Flask, render_template
from flask import request
from auction import get_superhero
import payabbhi
import string
import random
client = payabbhi.Client('<ACCESS-ID>','<SECRET-KEY>')

# create the application object
app = Flask(__name__)

@app.route('/')
def index():
    # The merchant_order_id is typically the identifier of the Customer Order, Booking etc in your system
    merchant_order_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    order = None
    error = None
    try:
        # Create the Payabbhi Order. Refer to Create Order API at https://payabbhi.com/docs/api/#create-an-order
        order = client.order.create(data={'merchant_order_id':merchant_order_id,'currency':'INR','amount':random.randint(100,500)})
        # TIP: At this point, the unique order_id should typically be persisted in your database against the merchant_order_id
    except Exception as e:
        error = e
    return render_template('index.html', access_id=client.access_id, merchant_order_id=merchant_order_id, order=order, error=error)  # render a template

# use decorators to link the function to a url
@app.route('/status', methods=['POST'])
def status():
    hero_name, hero_url = get_superhero()

    error = None
    payment = None

    try:
        # Here we verify the payment signature
        client.utility.verify_payment_signature({
            "order_id": request.form['order_id'],
            "payment_id": request.form['payment_id'],
            "payment_signature": request.form['payment_signature'] })

        # TIP: At this point we should typically look up the merchant_order_id corresponding to the order_id in the Payment response
        # The status of the order, booking etc identified by the merchant_order_id,
        # should be now updated in your database to indicate that it is paid.
        # You may also persist the payment_id in the database against the merchant_order_id.

        payment = client.payment.retrieve(request.form['payment_id'])

    except Exception as e:
        error = e
    return render_template('status.html', hero_url=hero_url, hero_name=hero_name, merchant_order_id=request.form['merchant_order_id'], payment=payment, error=error) # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
