from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONN_STRING']

engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_data_from_db_old():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())

  return (result_dicts)


def load_data_from_db():
  # Create a connection to the database.
  with engine.connect() as conn:

    # Execute a SQL query to select all rows from the `jobs` table.
    result = conn.execute(text("select * from jobs"))

    # Create a list to store the results of the query.
    result_dicts = []

    # Iterate over the results of the query and add each row to the list of dictionaries.
    for row in result.all():
      result_dicts.append(row._asdict())

    # Iterate over the results of the query and extract the salary  values.
    # Calculate the annual salary value and add it to each dictionary as the `annual_salary` key.
    for row in result_dicts:
      salary = row["salary"]
      total = salary * 12
      row["annual_salary"] = total

    # Return the list of dictionaries.
    return result_dicts


# function to get job by id
def get_job_by_id(id):
  with engine.connect() as conn:
    query = text("SELECT * FROM jobs WHERE id = :id")
    result = conn.execute(query, {"id": id})

  row = result.fetchone()

  if row is None:
    raise ValueError(f"Job ID {id} does not exist")
  else:
    return (row._asdict())
    
#function to search jobs by location
def search_jobs_by_location(location):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE LOWER(location) = LOWER(:location)")
        result = conn.execute(query, {"location": location})

    job_list = [row._asdict() for row in result]
    return job_list

#fucntion to search jobs either location wise or title wise
def search_jobs(title=None, location=None):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE LOWER(title) LIKE LOWER(:title) AND LOWER(location) LIKE LOWER(:location)")
        result = conn.execute(query, {"title": f"%{title}%" if title else "%", "location": f"%{location}%" if location else "%"})

    job_list = [row._asdict() for row in result]
    return job_list


