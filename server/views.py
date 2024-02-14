from flask import Flask, render_template
from models import Brand, Laptop, Phone

app = Flask(__name__)

@app.route('/laptop_page')
def laptop_page():
    brands = Brand.query.all()
    laptops = Laptop.query.all()
    return render_template('laptop_page.html', brands=brands, laptops=laptops)

@app.route('/phone_page')
def phone_page():
    brands = Brand.query.all()
    phones = Phone.query.all()
    return render_template('phone_page.html', brands=brands, phones=phones)

if __name__ == '__main__':
    app.run(debug=True)