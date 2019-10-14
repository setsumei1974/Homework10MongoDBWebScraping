#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
from splinter import Browser
import requests
from bs4 import BeautifulSoup

def scrape():


# In[20]:


    mars_omnibus = {}


# ### News about Mars from Nasa ###

# In[22]:


#Create an Executable Path to Chromedriver.exe and Select the Browser to Use with Splinter
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

#Use Browser from Splinter to Visit the Site of Nasa
    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)

#Parse the Site and Create an Object with Beautiful Soup
    soup = BeautifulSoup(browser.html, "html.parser")
#print(type(soup))

#Use BeautifulSoup to Navigate through the HTML of the Site to Locate Title and Paragraph
    news_title = soup.find("div", class_="content_title").get_text()
    news_paragraph = soup.find("div", class_="article_teaser_body").get_text()

    mars_omnibus["title"] = news_title
    mars_omnibus["paragraph"] = news_paragraph

#print(mars_omnibus)

    print(news_title)
    print(news_paragraph)


# ### Image of Mars from Jet Propulsion Laboratory ###

# In[23]:


#Create an Executable Path to Chromedriver.exe and Select the Browser to Use with Splinter
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

#Use Browser from Splinter to Visit the Site of Jet Propulsion Laboratory
    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_image_url)

#Parse the Site and Create an Object with Beautiful Soup
    soup = BeautifulSoup(browser.html, "html.parser")
#print(type(soup))

#Use BeautifulSoup to Navigate through the HTML of the Site to Locate the Featured Image
    featured_image_location = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + featured_image_location

    mars_omnibus["image"] = featured_image_url

#print(mars_omnibus)

    print(featured_image_url)


# ### Weather on Mars from Twitter ###

# In[24]:


#Create an Executable Path to Chromedriver.exe and Select the Browser to Use with Splinter
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

#Use Browser from Splinter to Visit the Site for Mars on Twitter
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)

#Parse the Site and Create an Object with Beautiful Soup
    soup = BeautifulSoup(browser.html, "html.parser")
#print(type(soup))

#Use BeautifulSoup to Navigate through the HTML of the Site to Locate the Tweet on Weather
    tweets = soup.find_all("div", class_="js-tweet-text-container")

    for tweet in tweets:
        mars_weather = tweet.find("p").text
        if "Sol" and "pressure" in mars_weather:
            print(mars_weather)
            break
        else:
            pass
    
    mars_omnibus["weather"] = mars_weather

#print(mars_omnibus)


# ### Facts about Mars from Space Facts ###

# In[25]:


#Create an Executable Path to Chromedriver.exe and Select the Browser to Use with Splinter
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

#Use Browser from Splinter to Visit the Site of Space Facts
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)

#Use the .read_html() Function of Pandas to Read the HTML Code of the Site
    mars_facts_read = pd.read_html(mars_facts_url)

#Use Pandas to Create a Dataframe
    mars_facts_df = pd.DataFrame(mars_facts_read[0])

#Organize the Dataframe, Name Columns, and Set the Index
    mars_facts_df.columns = ["Values", "Mars", "Earth"]
    mars_facts_df.set_index("Values", inplace=True)
    print(mars_facts_df)

#Use the .to_html() Function of Pandas to Convert the Dataframe to HTML Code
    mars_facts_html = mars_facts_df.to_html(header = False, index = False)

    mars_omnibus["facts"] = mars_facts_html

#print(mars_omnibus)

    print(mars_facts_html)


# ### Hemispheres of Mars from Astrogeology ###

# In[26]:


#Create an Executable Path to Chromedriver.exe and Select the Browser to Use with Splinter
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

#Use Browser from Splinter to Visit the Site of Astrogeology
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

#Parse the Site and Create an Object with Beautiful Soup
    soup = BeautifulSoup(browser.html, "html.parser")
#print(type(soup))

#Create an Empty Loop to Contain the Output of a For-Loop
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

#print(mars_omnibus)
    
    print(mars_hemispheres)

    return mars_omnibus

print(mars_onmibus)

