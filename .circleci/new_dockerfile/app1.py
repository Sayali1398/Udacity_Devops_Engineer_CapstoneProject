from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Rolling update done successfully!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=True)
