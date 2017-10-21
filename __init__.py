from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
	names = []
	for name in os.listdir("/Users/aditya/Projects/imager/static/images/"):
		names.append(name)

	return render_template("index.html", names = names)

@app.route('/editor',defaults={'path': ''})
@app.route('/editor/<path>')
def editor(path=""):
	if path == "":
		return render_template("editor.html")
	else:
		return render_template("editor.html", image = path)

if __name__=='__main__':
	app.run(debug=True)