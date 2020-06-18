# World Population Scrapy

Scrap world population from https://www.worldometers.info/world-population/population-by-country/ using Scrapy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some packages needed.

```bash
git clone git@github.com:sustiono/world-population-scrapy.git
cd world-population-scrapy
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
cd worldometers
pip install -r requirements.txt
```

## Usage
Choose one of the commands below to get the results in the desired format

```bash
scrapy crawl countries -o world_population.csv
scrapy crawl countries -o world_population.json
scrapy crawl countries -o world_population.xml
```