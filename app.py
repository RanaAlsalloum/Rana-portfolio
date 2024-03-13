from flask import Flask, render_template
app=Flask(__name__) # first flask app
projects = [
  {'id':1,
  'project':'web scrapping',
  'skills':'urllib python, python Requests,selenium,beautifulsoup'},
  {'id':2,
  'project':'AI model for flare mointoring',
  'skills':'python pandas, matblotlib,microsoft azure,pychatgpt'},
  

  
]
@app.route('/')
def hello_world():
  return render_template('home.html',myskills=projects,myname='Rana')
  

if __name__ == "__main__": 
  print("I'm inside the if now")
  app.run(host="0.0.0.0",port=True) # how to run the app


  