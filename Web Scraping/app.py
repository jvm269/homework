
# Dependencies and Setup
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars


# Flask Setup

app = Flask(__name__, template_folder='template')

# PyMongo Connection Setup

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Flask Routes
# Root Route to Query MongoDB & Pass Mars Data Into HTML Template: index.html to Display Data
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars, 
image1="https://resize.hswstatic.com/w_907/gif/mars-methane.jpg"
#mars_land ="https://news-cdn.softpedia.com/images/news2/here-are-the-real-mars-landscapes-featured-in-the-martian-493849-11.jpg"
#marsfax= "https://i.pinimg.com/originals/b9/fe/c5/b9fec5881b1838fa04e3880cc570e7ff.jpg"

 ) 

# Scrape Route to Import `scrape_mars.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# Define Main Behavior
if __name__ == "__main__":
    app.run()