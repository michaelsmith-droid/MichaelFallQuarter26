# import the Flask library into this file
from flask import Flask

# Create a new Flask app named "app"
app = Flask(__name__)

# Create a home page for our flask app (website)
@app.route('/') # The route for the home page
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True) 