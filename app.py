from flask import Flask, render_template

print( __name__ )

app = Flask(__name__)

@app.route('/')
def hello() :
    return '<h1 style = "color:green;" >Hello World !</h1>'


#<h1 style = "color:green" >hello world </h1>

if __name__ == '__main__' :
   app.run(port = 3030) 
    
    