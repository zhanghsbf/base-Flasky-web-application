from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Hello World!</h1>\n<font color=blue>blue font</font>"
@app.route("/user/<name>")
def user(name):
	return "<h1>Hello,%r!</h1>" %name

if __name__ == "__main__":
	app.run(debug=True)