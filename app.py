from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Durham_Tax_Scraper_DEF
import pymongo

app = Flask(__name__)
# Create connection variable

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/tax_app"
mongo = PyMongo(app)


# Connect to a database. Will create one if not already available.

# mongo = PyMongo(app)

@app.route("/")
def index():
    df = mongo.db.df.find()
    return render_template("index.html", df=df)

@app.route("/scrape")
def scraper():
    df = mongo.db.df
    tax_data = Durham_Tax_Scraper_DEF.tax()
    df.update({}, tax_data, upsert=True)
    return redirect("/", code=302)

if __name__== '__main__':
    app.run(debug=True)