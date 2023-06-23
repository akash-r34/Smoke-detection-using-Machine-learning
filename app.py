from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
LOGR = pickle.load(open(r'Model/LOGR.pkl','rb'))
NB = pickle.load(open(r'Model/NB.pkl','rb'))
RF = pickle.load(open(r'Model/RF.pkl','rb'))
SVMLK = pickle.load(open(r'Model/SVMLK.pkl','rb'))
SVMNLK = pickle.load(open(r'Model/SVMNLK.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/predict', methods =['POST'])#binds to an url
def login():
    try:
        Temp =request.form["Temperature[C]"]
        Hum =request.form["Humidity[%]"]
        TVOC =request.form["TVOC[ppb]"]
        eCO2 =request.form["eCO2[ppm]"]
        RawH2 =request.form["Raw H2"]
        RawEth =request.form["Raw Ethanol"]
        Press =request.form["Pressure[hPa]"]
        PM1 =request.form["PM1.0"]
        PM2 =request.form["PM2.5"]
        NC0 =request.form["NC0.5"]
        NC1 =request.form["NC1.0"]
        NC2 =request.form["NC2.5"]
        CNT =request.form["CNT"]
        model = request.form["model"]
    
        useModel = pickle.load(open(r'Model/'+model+'.pkl','rb'))
        
        test=[[float(Temp),float(Hum),int(TVOC),int(eCO2),int(RawH2),int(RawEth),float(Press),float(PM1),float(PM2),
               float(NC0),float(NC1),float(NC2),int(CNT)]]
        output= useModel.predict(test)
        print(output)  
            
        return render_template("booking.html",y = "Fire alarm triggers:  " + str(bool(output[0])))
    except:
        return render_template("404.html")

@app.route('/predict')#binds to an url
def predict():
    return render_template("booking.html")

@app.route('/404')#binds to an url
def error():
    return render_template("404.html")

@app.route('/contact')#binds to an url
def contact():
    return render_template("contact.html")

@app.route('/about')#binds to an url
def about():
    return render_template("about.html")

@app.route('/service')#binds to an url
def service():
    return render_template("service.html")

@app.route('/team')#binds to an url
def team():
    return render_template("team.html")

@app.route('/testimonial')#binds to an url
def testimonial():
    return render_template("testimonial.html")
#@app.route('/admin')#binds to an url
#def admin():
   # return "Hey Admin How are you?"

if __name__ == '__main__' :
    app.run(debug= False)
    


