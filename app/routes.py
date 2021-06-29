
from flask import Flask, request
from app.database import (
    scan, insert, 
    deactivate_user
    )

app =Flask(__name__)

app = Flask(__name__)

@app.route("/")
def get_index():
    return render_templates("index.html")
    
@app.route("/users")
def GET_all_users():
    out = {
        "ok": True,
        "Message": "Success"
    } 
    out["body"] = scan()
    #retreive list of users
    return out 

@app.route("/users", methods=["POST"])
def create_user():
    out = {
    "ok": True,
    "Message": "Success"
    } 
    user_data = request.json
    out["last_row_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        user_data.get("active"),
    )
    return out, 201

@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    out = {
    "ok": True,
    "Message": "Success"
    } 
    deactivate_user(uid)
    return out, 204

        
@app.route('/agent')
def agent():
    user_agent = request.headers.get("csrftoken")
    return "<p>Your user agent is: %s</p>" % user_agent