from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection details
host = 'WorldWired.mysql.pythonanywhere-services.com'
user = 'WorldWired'
password = 'SharatTovMeod7430685'
database = 'bravery_data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']

    # Establish a connection
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    try:
        with connection.cursor() as cursor:
            # Check if the user exists in the database
            sql = 'SELECT * FROM users WHERE username = %s AND password = %s'
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()

            if result:
                return "Login successful!"
            else:
                return "Invalid username or password"
    finally:
        # Close the connection
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
