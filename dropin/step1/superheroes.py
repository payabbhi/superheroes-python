# import the Flask class from the flask module
from flask import Flask, render_template
from flask import request
import payabbhi
import string
import random
client = payabbhi.Client('<ACCESS-ID>','<SECRET-KEY>')

# create the application object
app = Flask(__name__)

@app.route('/')
def index():
    d = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    order = client.order.create(data={'merchant_order_id':d,'currency':'INR','amount':random.randint(100,500)})
    return render_template('index.html', access_id=client.access_id, merchant_order_id=d, order=order)  # render a template

# use decorators to link the function to a url
@app.route('/status', methods=['POST'])
def status():
    heroes = {
    'Batman'         : 'https://upload.wikimedia.org/wikipedia/en/thumb/2/22/Batman-DC-Comics.jpg/250px-Batman-DC-Comics.jpg',
    'Superman'       : 'https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/SupermanRoss.png/250px-SupermanRoss.png',
    'Aquaman'        : 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0a/Aquaman_issue_1%2C_the_new_52.jpg/220px-Aquaman_issue_1%2C_the_new_52.jpg',
    'Spiderman'      : 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Spiderman50.jpg/250px-Spiderman50.jpg',
    'Wonder Woman'   : 'https://upload.wikimedia.org/wikipedia/en/0/03/Wonder_Woman_%28DC_Rebirth%29.jpg',
    'Iron Man'       : 'https://i.annihil.us/u/prod/marvel//universe3zx/images/f/f5/IronMan_Head.jpg',
    'Hulk'            : 'https://upload.wikimedia.org/wikipedia/en/5/59/Hulk_%28comics_character%29.png',
    'Captain America' : 'https://upload.wikimedia.org/wikipedia/en/thumb/9/91/CaptainAmerica109.jpg/250px-CaptainAmerica109.jpg',
    'Falcon'          : 'https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/TheFalcon.jpg/250px-TheFalcon.jpg',
    'Wasp'            : 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/AVEN071.jpg/250px-AVEN071.jpg',
    'Quicksilver'     : 'https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Quicksilver%21.jpg/250px-Quicksilver%21.jpg',
    'Doctor Strange'  : 'https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/Doctor_Strange_Vol_4_2_Ross_Variant_Textless.jpg/250px-Doctor_Strange_Vol_4_2_Ross_Variant_Textless.jpg',
    'Hawkeye'         : 'https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Hawkeye_%28Clinton_Barton%29.png/220px-Hawkeye_%28Clinton_Barton%29.png',
    'Wolverine'       : 'https://upload.wikimedia.org/wikipedia/en/c/c8/Marvelwolverine.jpg',
    'Black Widow'     : 'https://i.annihil.us/u/prod/marvel//universe3zx/images/f/f9/BlackWidow.jpg',
  }

    hero_name, hero_url = random.choice(list(heroes.items()))
    payment_id = request.form['payment_id']
    merchant_order_id = request.form['merchant_order_id']
    return render_template('status.html', hero_url=hero_url, hero_name=hero_name, payment_id=payment_id, merchant_order_id=merchant_order_id) # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
