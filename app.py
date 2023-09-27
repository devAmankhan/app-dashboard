import psycopg2
from flask import Flask, render_template

# Connect to the database
conn = psycopg2.connect(
    host="tensordb1.cn6gzof6sqbw.us-east-2.rds.amazonaws.com",
    port=5432,
    database="postgres",
    user="admin123",
    password="tensor123",
)

# Create a cursor to execute queries
cur = conn.cursor()

# Execute the query
cur.execute(
    "SELECT max(timestamp), forecast_method FROM forecast.db_api GROUP BY forecast_method"
)

# Fetch the results
results = cur.fetchall()

# Create a web page to display the results
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", results=results)


# Serve the web page to the user
if __name__ == "__main__":
    app.run()
