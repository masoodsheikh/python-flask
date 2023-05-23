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

    # Iterate over the results of the query and extract the qty and rate values.
    # Calculate the total value and add it to each dictionary as the `total` key.
    for row in result_dicts:
      salary = row["salary"]
      total = salary * 12
      row["annual_salary"] = total

    # Return the list of dictionaries.
    return result_dicts

