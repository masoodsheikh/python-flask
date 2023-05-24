from flask import Flask, render_template, jsonify
from database import load_data_from_db, get_job_by_id, search_jobs_by_location, search_jobs


app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_data_from_db()
  return render_template('home.html', jobs=jobs)


#api for getting all jobs
@app.route("/api/jobs")
def list_jobs():
  jobs = load_data_from_db()
  return jsonify(jobs)


#api for getting job by id
@app.route("/getJobById/<id>")
def getJobById(id):
  try:
    job = get_job_by_id(int(id))
  except ValueError:
    return jsonify({"error": "Job ID does not exist"})
  else:
    return jsonify(job)


#api for getting job by location
@app.route("/getJobsByLocation/<location>")
def getJobsByLoction(location):
  try:
    jobs = search_jobs_by_location(location)
  except ValueError:
    return jsonify({"error": "No Jobs Found"})
  else:
    return jsonify(jobs)


#api for getting job by location or title

from urllib.parse import unquote_plus


@app.route("/searchJobs/<search_query>")
def searchJobs(search_query):
  search_query = unquote_plus(search_query)
  params = search_query.split("/")
  title = params[0] if params[0] != "none" else None
  location = params[1].replace(
    "%20", " ") if len(params) > 1 and params[1] != "none" else ""

  if not title and not location:
    return jsonify({"error": "Please provide either a title or location."})

  job_list = search_jobs(title=title, location=location)
  return jsonify(job_list)




if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
