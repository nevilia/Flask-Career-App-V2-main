from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs 10,00,000'
    },
    {
        'id': 2,
        'title': 'Front-End Engineer',
        'location': 'Gurgaon,India',
        'salary': 'Rs 15,00,000'
    },
    {
        'id': 3,
        'title': 'Back-End Engineer',
        'location': 'Chennai, India',
        'salary': 'Rs 18,00,000'
    },
    {
        'id': 4,
        'title': 'Marketing Head',
        'location': 'Seattle, US',
        'salary': '$ 100,000'
    },
    {
        'id': 5,
        'title': 'Cloud Engineer',
        'location': 'Seattle, US',
        'salary': '$ 120,000'
    },
    {
        'id': 6,
        'title': 'Database Administrator',
        'location': 'Bengaluru, India',
        'salary': 'Rs 12,00,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
