from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [

  {
    'id':1,
    'title':'Data Anyalist',
    'location':'Lahore',
    'salary':'Rs. 500,000/-'
  },
  {
    'id':2,
    'title':'Front End Developer',
    'location':'Faisalabad',
    'salary':'Rs. 400,000/-'
  },
  {
    'id':3,
    'title':'Back End Developer',
    'location':'Islamabad',
    'salary':'Rs. 600,000/-'
  },
  {
    'id':4,
    'title':'Full Stack Developer',
    'location':'Karachi',
    'salary':'Rs. 700,000/-'
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
    
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)