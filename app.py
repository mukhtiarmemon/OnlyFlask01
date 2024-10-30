from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Again with Flask Public Apppp!"

if __name__ == "__main__":
    # Set the host to '0.0.0.0' to make it accessible externally, or use '127.0.0.1' for local access only
    # Specify port 8080 (or any other preferred port)
    app.run(host="0.0.0.0", port=8080)