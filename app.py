from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    # Render the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application on a local development server
    app.run(debug=True)
