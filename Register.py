from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

host = 'WorldWired.mysql.pythonanywhere-services.com'
user = 'WorldWired'
password = 'SharatTovMeod7430685'
database = 'bravery_data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Existing login code (check username and password against the database)
    pass

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the registration form
    Username = request.form['username']
    Password = request.form['password']

    # Establish a connection
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    try:
        with connection.cursor() as cursor:
            # Check if the username already exists in the database
            sql_check_user = 'SELECT * FROM users WHERE username = %s'
            cursor.execute(sql_check_user, (Username))
            existing_user = cursor.fetchone()

            if existing_user:
                return "Username already exists. Choose another username."
            
            # If the username doesn't exist, insert the new user into the 'users' table
            sql_insert_user = "INSERT INTO users (Username, Password) VALUES (%s, %s)"
            cursor.execute(sql_insert_user, (Username, Password))
            
            # Commit the changes to the database
            connection.commit()

            return "Registration successful. You can now log in."
    finally:
        # Close the connection
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
