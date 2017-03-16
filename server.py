from flask import Flask, request
from random import choice, randint
from flask import render_template

COMPLIMENTS = ["smart", "clever", "tenacious",
                "awesome", "Pythonic"]


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def index():
    """Home page."""

    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
            Say hello
        </body>
    </html>
    """
    return html

@app.route('/lucky')
def lucky_number():
    lucky_num = randint(1, 100)
    lucky_message = "Your lucky number is %s " % lucky_num
    return "<html><body><h1>" + lucky_message + "</h1></body></html>"

    """Provides a random lucky number"""
    # add code here of getting a lucky number and return a string
    # with the lucky number

@app.route('/puppies_or_kittens')
def puppies_or_kittens():
    buttons = """
        <html>
            <body>
                <a href=/puppy> <button type='button'> Click here to see a PUPPY!</button> </a></br>
                <a href=/kitten> <button type='button'> click me for a kitten! </button></a>
            </body>
        </html>   
            """
    return buttons

@app.route('/puppy')
def show_puppy():
    #html with the puppy image
    puppy = """
    <html>
        <body>
            <img src = "https://ipetcompanion.com/feedapuppy/styles/media/puppy.jpg"><br>
            <h3><a href =/puppies_or_kittens>Take me back!</a></h3>
        </body>
    </html>
    """
    return  puppy
    #link to the route puppies or kittens

@app.route('/kitten')
def show_kitten():
    kitten = """
    <html>
        <body>
         <img src = http://s3.amazonaws.com/assets.prod.vetstreet.com/2a/cd/ee484be546418f40cc3cbc194b52/kitten-in-arms-thinkstockphotos-106397271-335lc070915jpg.jpg>
         <h3><a href = /puppies_or_kittens>Take me back!</a><h3>
        </body>
    </html>
    """
    return kitten

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/greet')
def greet():
    player = request.args.get("person")
    nice_thing = choice(COMPLIMENTS)
    return render_template("compliments.html",
        name=player,
        compliment=nice_thing)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
