from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_all_currencies():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    return sorted(response.json()["rates"].keys())

def get_currency_names():
    return {
        'USD': 'US Dollar',
        'EUR': 'Euro',
        'GBP': 'British Pound',
        'JPY': 'Japanese Yen',
        'AUD': 'Australian Dollar',
        'CAD': 'Canadian Dollar',
        'CHF': 'Swiss Franc',
        'CNY': 'Chinese Yuan',
        'INR': 'Indian Rupee',
        'SGD': 'Singapore Dollar',
        'NZD': 'New Zealand Dollar',
        'MXN': 'Mexican Peso',
        'BRL': 'Brazilian Real',
        'ZAR': 'South African Rand',
        'RUB': 'Russian Ruble',
        'KRW': 'South Korean Won',
        'TRY': 'Turkish Lira',
        'AED': 'UAE Dirham',
        'SAR': 'Saudi Riyal',
        # Add more as needed
    }

def get_flag_emoji(currency_code):
    flag_map = {
        'USD': '🇺🇸', 'EUR': '🇪🇺', 'GBP': '🇬🇧',
        'JPY': '🇯🇵', 'AUD': '🇦🇺', 'CAD': '🇨🇦',
        'CHF': '🇨🇭', 'CNY': '🇨🇳', 'INR': '🇮🇳',
        'SGD': '🇸🇬', 'NZD': '🇳🇿', 'MXN': '🇲🇽',
        'BRL': '🇧🇷', 'ZAR': '🇿🇦', 'RUB': '🇷🇺',
        'KRW': '🇰🇷', 'TRY': '🇹🇷', 'AED': '🇦🇪',
        'SAR': '🇸🇦'
    }
    return flag_map.get(currency_code, '🌐')

@app.route("/", methods=["GET", "POST"])
def home():
    currencies = get_all_currencies()
    currency_names = get_currency_names()
    
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            base = request.form["base"].upper()
            target = request.form["target"].upper()
            
            rate = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base}").json()["rates"][target]
            result = amount * rate
            
            return render_template(
                "index.html",
                currencies=currencies,
                currency_names=currency_names,
                result=f"{amount} {base} = {result:.2f} {target}",
                base_currency=base,
                target_currency=target
            )
        except Exception as e:
            return render_template(
                "index.html",
                currencies=currencies,
                currency_names=currency_names,
                error=f"Error: {str(e)}"
            )
    
    return render_template(
        "index.html",
        currencies=currencies,
        currency_names=currency_names
    )

if __name__ == "__main__":
    app.run(debug=True)






 #http://localhost:5000ht
