from flask import Flask, render_template
import pymongo
import ScrapeMars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.produce

@app.route("/")
def index():

    mars_omnibus = db.collection.find()

    return render_template("index.html", mars_omnibus=mars_omnibus)

@app.route("/scrape")
def Scrape():

    mars_omnibus = mongo.db.collection
    mars_data = ScrapeMars.ScrapeMarsNews()
    mars_data = ScrapeMars.ScrapeMarsImage()
    mars_data = ScrapeMars.ScrapeMarsWeather()
    mars_data = ScrapeMars.ScrapeMarsFacts()
    mars_data = ScrapeMars.ScrapeMarsHemispheres()
    mars_omnibus.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)