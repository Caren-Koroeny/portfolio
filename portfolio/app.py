from flask import Flask,render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")
#render_template() searches for the highlighted template HTML file within the template folder.
#in this case it will allow me to view the linked HTML file which is home here..
@app.route("/about")
def about ():
    return render_template("about.html")

@app.route("/log_in")
def login():
    return render_template("log_in.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/services")
def services():
    return render_template("services.html")

if __name__== "__main__":
    app.run(debug=True)
    
    
    
    #This is the python script which incoorporate all the pages created.