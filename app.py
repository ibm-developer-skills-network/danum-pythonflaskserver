from flask import Flask

app = Flask("My Flask Application")

@app.route("/")
def hello():
    return "<h1>My First Hello World!</h1>"

if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000
