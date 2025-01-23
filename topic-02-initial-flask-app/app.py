from flask import  Flask, render_template

# just imported pets db from first class to do some stuffs
import sqlite3
connection = sqlite3.connect("pets.db",check_same_thread=False) #database connection


app = Flask(__name__)

@app.route("/", methods=["GET"]) # This is a 'decoration' --connects routes to function
#this is called index route now
def get_index():
    return("example server")

@app.route("/hello", methods=["GET"]) # This is a 'decoration' --connects routes to function
@app.route("/hello/<name>", methods=["GET"]) # This is a 'decoration' --connects routes to function
def get_hello(name = "world"):
    data = [
        {"name":"Bibek","age":26},
        {"name":"Sujan","age":29},
    ]
    return render_template("hello.html", data=data, prof={"name":name, "title":"Dr."})
    # return render_template("hello.html", name=name)
    #return("hello " + name + "!")

@app.route("/bye", methods=["GET"])
def get_bye():
    return("Bye")

@app.route("/list", methods=["GET"])
def get_list():
    cursor = connection.cursor()
    #fetching records
    cursor.execute("""select * from pets where type = ?""",("dog",)) #in tuple, always put a comma
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render_template("list.html", rows=rows)
    
# @app.route("/list", methods=["GET"])
# def get_list():
#     cursor = connection.cursor()
#     cursor.execute("""select * from pets where type=?""",("dog",))
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     return render_template("list.html", rows=rows)       