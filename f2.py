from flask import Flask,render_template,request 

app = Flask(__name__) 

@app.route("/") 

def home(): 
    return render_template("form.html") 

@app.route("/Submit",methods=["POST"]) 

def Submit(): 
    if request.method == 'POST':
        name = request.form["name"]
        return  render_template("form.html",text = name)
    
if __name__=="__main__": 
    app.run(debug=True)