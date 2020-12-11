from flask import Flask, render_template, jsonify, request
import json
import random

app = Flask(__name__)

fin = [
    {
        "country": "USA",
        "ranking": 8,
        "shift": "Right",
        "party": "Republican Party",
        "shiftpara": "Over the past four decades – and more sharply over just the past few years – the geopolitical center of America has shifted rightward. It hasn't happened on all fronts – certainly, there are some areas where the country has clearly moved to the left, such as views on gay rights. But on a host of other issues, from guns to the role of government, the center of debate has edged closer to the conservative position, while activists on the right have moved even further out on the political spectrum.",
        "lgbtq": "President Trump has actively worked against LGBTQ rights, in particular trans rights, since he took office in 2017. His ban on transgender people in the military had reached headlines during his presidency, and government agencies have moved to reduce the visibility and acknowledgement of sexual minorities on official documents.", 
        "foreign": "Trump's America First policies famously includes comprehensive border control with Mexico. His critique against involvement in international organizations and global cooperation through bodies like the World Health Organization, NATO, and treaties such as the Paris Climate Accords and Iranian denuclearization indicate a retreat from global affairs.",
        "economic": "Trump's tariffs and trade war with China signals opposition to globalization, and his tax cuts and coronavirus relief for corporations indicates his strong support for American corporations.", 
        "religion": "Trump has defended religious liberty through appointment of conservative jurists to federal courts, but he has been very anti-Islam and has perpetrated islamophobia across the country."
    },
    {
        "country": "Canada",
        "ranking": 2,
        "shift": "Left",
        "party": "Liberal Party", 
        "shiftpara": ""
    },
    {
        "country": "Mexico",
        "ranking": 6,
        "shift": "Left",
        "party": "MORENA"
    },
    {
        "country": "UK",
        "ranking": 6,
        "shift": "Right",
        "party": "Conservative Party"
    },
    {
        "country": "Brazil",
        "ranking": 10,
        "shift": "Far-Right"
    },
    {
        "country": "Turkey",
        "ranking": 8,
        "shift": "Far-Right",
        "party": "JDP",
        "immigration": "Since 2014, Turkey has hosted the world’s largest refugee population, and though it has issues with providing equitable care for these displaced peoples, they have been a model for accepting refugees.", 
        "shiftpara": "According to the Guardian, '[Erdogan's] most recent term in office was the most populist of any rightwing leader in the Global Populism Database, which tracks the levels of populist discourse in the speeches of almost 140 leaders in Europe and the Americas.' The purges following a suppressed coup and strengthening the executive branch may indicate authoritarian leanings of Erdogan's populism.",
        "lgbtq": "Erdogan's administration has enforced a an on LGBT cultural events, and stated that LGBT empowerment 'against the values of our nation.'", 
        "foreign": "Turkey has in recent years looked for greater regional cooperation, including with the EU and Mediterranean neighbors.", 
        "economic": "The Turkish economy has been stagnant in recent years. Its economic stagnation drives desire for strong economic leadership."
    },
    {
        "country": "Hungary",
        "ranking": 7,
        "shift": "Far-Right",
        "party": "Fidesz"
    },
    {
        "country": "Philippines",
        "ranking": 3,
        "shift": "Left",
        "party": "PDP-Laban"
    },
    {
        "country": "India",
        "ranking": 8,
        "shift": "Right",
        "party": "BJP"
    },
    {
        "country": "Australia",
        "ranking": 2,
        "shift": "Left",
        "party": "Liberal"
    },
    {
        "country": "New-Zealand",
        "ranking": 1,
        "shift": "Far-Left",
        "party": "Labour"
    },
    {
        "country": "Italy",
        "ranking": 6,
        "shift": "Centre"
    },
    {
        "country": "France",
        "ranking": 7,
        "shift": "Centre-Right"
    },
    {
        "country": "Germany",
        "ranking": 4,
        "shift": "Centre-Right"
    },
    {
        "country": "Poland",
        "ranking": 9,
        "shift": "Right"
    }
]

countries = ["United States", "Canada", "Mexico", "UK", "Brazil", "Turkey", "Hungary", "Philippines", "India", "Australia", "New Zealand", "Italy", "France", "Germany", "Poland"]

points = [8,2,6,6,10,8,7,3,8,2,1,6,7,4,9]

shift = ["Right", "Left", "Left", "Right", "Far-Right", "Far-Right", "Far-Right", "Left", "Right", "Left", "Far-Left", "Center", "Centre-Right", "Centre-Right", "Right"]

random.seed(50) 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results')
def results(): 
    return "results"


curr = list()

for i in range(len(countries)):
    temp = {}
    temp["country"] = countries[i]
    temp["ranking"] = points[i]
    temp["shift"] = shift[i]
    curr.append(temp)

@app.route('/api', methods = ['GET', 'POST'])
def api():
    if request.method != "POST":
        return "invalid request"
    return jsonify(fin)

@app.route('/ranking', methods = ['GET', 'POST'])
def ranking():
    return render_template("ranking.html", fin = fin)

@app.route('/credits')
def credits():
    return "credits"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)