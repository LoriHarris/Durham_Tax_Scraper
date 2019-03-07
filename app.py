from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Durham_Tax_Scraper_DEF
import pymongo
import cgi

app = Flask(__name__)
# Create connection variable

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/tax_app")



# Connect to a database. Will create one if not already available.

# mongo = PyMongo(app)

@app.route("/")
def index():
    form = cgi.FieldStorage()
    address =  form.getvalue('searchbox')
    tax_info = mongo.db.collection.find_one()
    return render_template("index.html", data=tax_info, address=address)

@app.route("/scrape")
def scraper():
    # df = mongo.db.df
    df = Durham_Tax_Scraper_DEF.tax()
    mongo.db.collection.update({}, df, upsert=True)
    
    return redirect("/", code=302)

if __name__== '__main__':
    app.run(debug=True)