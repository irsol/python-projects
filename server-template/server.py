from flask import Flask
from flask import jsonify
from flask import render_template
from db import connect, execute_sql

app = Flask(__name__)

# Database name specified in Vagrantfile, for example "db_template"
connection = connect(db_name='db_template')


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/nice_page')
def nice_page():
    return render_template('nice_page.html')


@app.route("/get_users")
def get_users():
    sql = "SELECT user_name, age FROM users"

    results = execute_sql(sql, connection)
    
    # Example of the output format
    # {
    #     'users': [
    #         {
    #             'name': 'Tom',
    #             'age': 222
    #         }
    #     ]
    # } 

    # create a dictionary with one key "users" and empty list as a value
    output = {
        'users': []
    }

    # add dictionary with user name and age to the list created above
    for name, age in results:
        output['users'].append({
            'name': name,
            'age': age
        })

    # convert Python dict to JSON object and set appropriate HTTP headers:
    # "Content-Type:application/json"
    return jsonify(output)
