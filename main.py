from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print("\n New Form Submission:")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return f"""
        <h2>Thank you, {name}!</h2>
        <p>Your message has been received.</p>
        <a href="/home">Go back to Homepage</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
