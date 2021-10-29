from flask import Flask, render_template


#create flask instance
app = Flask(__name__)

#create route 

@app.route('/')

#def index():
   # return '<h1>Hello World!</h1>'
def index():
    first_name= 'john'

    favorite_pizza=["pepperoni, cheese, meat,pinaapple"]
    return render_template("index.html",
     first_name=first_name,
     favorite_pizza=favorite_pizza)
     


#Localhost:5000/user/Edgard
@app.route('/user/<name>')

def user(name):
  return render_template("user.html", user_name=name)
 
 #Create  custom error pgs thing
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500



