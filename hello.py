from flask import Flask, render_template


# Create Flask Instance
app = Flask(__name__)				#this helps flask found our project

# Create a route decorator
@app.route('/')						#index page / home page

#def index():						#function declaration of index
#	return "<h1>Hello World!</h1>"	#h1 is heaader 1, h2 h3 and so on is getting smaller than h1

#FILTERS!!!
#safe
#capitalize
#lower
#upper
#title
#trim			remove last space
#striptags

def index():						#function declaration of index
	first_name = "John"
	stuff = "This is <strong>bold</strong> text"
	stuff2 = "This is bold text"
	favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
	return render_template("index.html", 
		first_name=first_name, 					#render template in templates folder/ index.html, pass firs_name variable
		stuff=stuff, 
		stuff2=stuff2, 
		favorite_pizza=favorite_pizza)			#we also can pass dictionary and array of data
																
# localhost:5000/user/john
@app.route('/user/<name>')							#index page / home page

def user(name):										#function declaration of index
	return render_template("user.html", user_name=name)	#render template in templates folder/ user.html

# Create Custom Error Pages

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

#if __name__ == "__main__":
#	app.run(debug=True)								#automatically rerun if detect any changes  (debug mode)