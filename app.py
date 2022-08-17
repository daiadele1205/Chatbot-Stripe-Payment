# Create app.py and set up Stripe’s configuration

import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

# Create Flask methods, to display payment form, and accept charges

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)


    # Run the app.py
    # PUBLISHABLE_KEY=pk_test_51LXQ8kBFCLxXm5AIuzpvP7MnU1quJTK7Ng9l2fSWsGNtZQd05ckBPjRm6YEgYVBE9VQ2Jg9dHzbB6HjnXxQPQSmt00tkCHFW7V SECRET_KEY=sk_test_51LXQ8kBFCLxXm5AI5Bti5nzjnhLBXVxdNcJLVfP3I6HJacnYx7NxyrslnIH5CoHi46hkJKUd3WJU9EigVI3gJ3Kl00Q64Mod5q python app.py