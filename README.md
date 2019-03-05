# Scrapy Project

### Overview
This Scrapy project show how to scrape the website(http://quotes.toscrape.com/).

### Requirements
* Python : 3.6.5
* Scrapy : 1.5.1
* System : Mac OSX 10.14.3


# Install
* Clone repository or down zip file directly:
````
$ git clone url(git's url)
````
* Install virtual virtualenv
````
$ pip3 install virtualenv
````
* Create virtualenv
````
$ python3 -m venv vnev
````
* Activate virtual env
````
$ . venv/bin/activate
````
* Install requirements.txt on virtual environment.
````
$  pip3 install -r requirements.txt
````

# Getting Start
Now, you can use scrapy to scrape data.
````
$ cd myproject
$ scrapy crawl mybot
````
If you want to store the result into the format for csv, just follow below:
````
$ scrapy crawl mybot -o [your_file name]
````
These formats are supported out of the box: 
* JSON
* JSON lines
* CSV
* XML

# Commercial Support
Link : http://doc.scrapy.org/en/latest/index.html

