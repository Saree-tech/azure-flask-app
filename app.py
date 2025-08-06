from flask import Flask, render_template
import os

app = Flask(__name__)

# Use environment variable for the site title
SITE_TITLE = os.getenv("SITE_TITLE", "My Flask Site")

@app.route('/')
def home():
    return render_template("index.html", title=SITE_TITLE)

@app.route('/about')
def about():
    return render_template("about.html", title=SITE_TITLE)

@app.route('/contact')
def contact():
    return render_template("contact.html", title=SITE_TITLE)

if __name__ == '__main__':
    app.run()
