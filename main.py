from flask import Flask,jsonify,request
from filtered_stars import data
app = Flask(__name__)

@app.route("/")
def main():
    return jsonify({
        "filtered_stars":data,
        "message":"sucess"
    }),200
@app.route("/star")
def stars():
    name = request.args.get("Star_name")
    star_data = next(item for item in data if item["Star_name"] == name)
    return jsonify({
        name:star_data,
        "message":"sucess"
    }),200
@app.route("/test")
def testing():
    return "works"
app.run(debug = True)