from flask import Flask, render_template
app=Flask(__name__) # first flask app

@app.route('/')
def hello_world():
  return render_template('home.html')
  

if __name__ == "__main__": 
  print("I'm inside the if now")
  app.run(host="0.0.0.0",port=True) # how to run the app


  