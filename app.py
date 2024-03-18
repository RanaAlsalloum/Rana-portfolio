from flask import Flask, render_template
from database import load_project_from_db
app=Flask(__name__) # first flask app


  

@app.route('/')
def hello_world():
  projects = load_project_from_db()
  return render_template('home.html',myskills=projects,myname='Rana')
  

if __name__ == "__main__": 
  print("I'm inside the if now")
  app.run(host="0.0.0.0",port=True) # how to run the app


  