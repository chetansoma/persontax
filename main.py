from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/tax', methods=['POST'])  # This will be called from UI
def PersonalTax():  # This is to calculate UK personal tax for year 2022/2023
    if (request.method == 'POST'):
        sal = float(request.form['sal'])
        div = float(request.form['div'])
        rent = float(request.form['rent'])
        rent_exp = float(request.form['rent_exp'])
        if rent > 640:
            rent_income = rent - rent_exp - 640
        if rent <= 640:
            rent_income = rent - rent_exp
        yr_allowance = 12500
        rent_tax = rent_income * .2
        rent_sal_tax = rent_tax + (sal - yr_allowance) * .2
        tax = rent_sal_tax + (div - 2000) * .075
        return render_template('results.html', result=tax, result1=rent_income, result2=rent_tax)


if __name__ == '__main__':
    app.run()
