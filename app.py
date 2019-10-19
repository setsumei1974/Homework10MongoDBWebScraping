from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import ScrapeMars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars_omnibus = mongo.db.mars_omnibus.find_one()
   return render_template("index.html", mars_omnibus=mars_omnibus)

@app.route("/scrape")
def Scrape():
   mars_omnibus = mongo.db.mars_omnibus
   mars_data = ScrapeMars.Scrape()
   mars_omnibus.update({}, mars_data, upsert=True)
   return redirect("/", code=302)

if __name__ == "__main__":
   app.run(debug=True)