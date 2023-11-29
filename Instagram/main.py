from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "sunnyjangra424006",
    "database": "sunnydb",
}

# Function to execute SQL queries
def execute_query(query, data=None):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

# Route to render the user input form
@app.route("/")
def index():
    return render_template("add_user.html")

# Route to handle form submission and insert data into the database
@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        query = """
            INSERT INTO instagram 
            (username, password) 
            VALUES (%s, %s)
        """
        data = (username, password)
        execute_query(query, data)

        return render_template("add_user.html")

if __name__ == "__main__":
    app.run(debug=True)
