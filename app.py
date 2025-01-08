from flask import Flask , render_template ,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'ML Engineer',
    'location' : 'Islamabad , Pakistan',
    'salary' : 'Rs. 70000'
  }, 
  {
    'id':2,
    'title' : 'Android Developer',
    'location' : 'Rawalpindi , Pakistan',
    'salary' : 'Rs. 40000'
  },
  {
    'id': 3,
    'title' : 'PHP Developer',
    'location': 'Lahore , Pakistan',
    'salary' : 'Rs. 65000'
  },
  {
    'id': 4,
    'title' : 'Data Scientist',
    'location': 'Karachi , Pakistan',
    'salary' : 'Rs. 80000'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html' ,
                         jobs=JOBS)

@app.route("/api/jobs")
def listjobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
