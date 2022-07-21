from flask import Flask, render_template
app = Flask(_name_)

@app.route("/")
def hello():
  return "Hello world, this is flask app home page"

if _name_ == "_main_":
  app.run(debug=True)
