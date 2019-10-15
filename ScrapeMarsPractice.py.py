import pandas as pd
from splinter import Browser
import requests
from bs4 import BeautifulSoup

def InitializeBrowser():

    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

mars_omnibus = {}

def ScrapeMarsNews():

    try:
        
        browser = InitializeBrowser()

        mars_news_url = "https://mars.nasa.gov/news/"
        browser.visit(mars_news_url)

        soup = BeautifulSoup(browser.html, "html.parser")

        news_title = soup.find("div", class_="content_title").get_text()
        news_paragraph = soup.find("div", class_="article_teaser_body").get_text()

        mars_omnibus["title"] = news_title
        mars_omnibus["paragraph"] = news_paragraph

        return mars_omnibus

    finally:

        browser.quit()

def ScrapeMarsImage():

    try:

        browser = InitializeBrowser()       
        
        mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(mars_image_url)

        soup = BeautifulSoup(browser.html, "html.parser")

        featured_image_location = soup.find("img", class_="thumb")["src"]
        featured_image_url = "https://www.jpl.nasa.gov" + featured_image_location

        mars_omnibus["image"] = featured_image_url

        return mars_omnibus

    finally:

        browser.quit()

def ScrapeMarsWeather():

    try:

        browser = InitializeBrowser()

        mars_weather_url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(mars_weather_url)

        soup = BeautifulSoup(browser.html, "html.parser")

        tweets = soup.find_all("div", class_="js-tweet-text-container")

        for tweet in tweets:
            mars_weather = tweet.find("p").text
            if "Sol" and "pressure" in mars_weather:
                print(mars_weather)
                break
            else:
                pass
        
        mars_omnibus["weather"] = mars_weather

        return mars_omnibus

    finally:

        browser.quit()

def ScrapeMarsFacts():

    try:

        browser = InitializeBrowser()        
        
        mars_facts_url = "https://space-facts.com/mars/"
        browser.visit(mars_facts_url)

        mars_facts_read = pd.read_html(mars_facts_url)

        mars_facts_df = pd.DataFrame(mars_facts_read[0])

        mars_facts_df.columns = ["Values", "Mars", "Earth"]
        mars_facts_df.set_index("Values", inplace=True)

        mars_facts_html = mars_facts_df.to_html(header = False, index = False)

        mars_omnibus["facts"] = mars_facts_html

        return mars_omnibus

    finally:

        browser.quit()

def ScrapeMarsHemispheres():

    try:

        browser = InitializeBrowser()

        mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(mars_hemispheres_url)

        soup = BeautifulSoup(browser.html, "html.parser")

        mars_hemispheres = []

        products = soup.find("div", class_="result-list")
        hemispheres = products.find_all("div", class_="item")

        for hemisphere in hemispheres:
            title = hemisphere.find("h3").text
            title = title.replace("Enhanced", "")
            end_link = hemisphere.find("a")["href"]
            image_link = "https://astrogeology.usgs.gov/" + end_link    
            browser.visit(image_link)
            soup = BeautifulSoup(browser.html, "html.parser")
            downloads = soup.find("div", class_="downloads")
            image_url = downloads.find("a")["href"]
            mars_hemispheres.append({"title": title, "img_url": image_url})

        mars_omnibus["hemispheres"] = mars_hemispheres

        return mars_omnibus

    finally:

        browser.quit()

print(mars_omnibus)