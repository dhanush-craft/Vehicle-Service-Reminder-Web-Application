from flask import Flask,render_template,url_for,request
from datetime import datetime,timedelta
from urllib.parse import urlencode
app = Flask(__name__)

@app.route('/', methods=["GET" ,"POST"])
def index ():
    dateof = ""
    dayz=""
    enddate=""
    link=""
    if request.method == "POST":
        try:
            dateof=request.form.get('dateof')
            date = datetime.strptime(dateof,"%Y-%m-%d")
            dayz=int(request.form.get('dayz'))
            enddate = (date + timedelta(days=dayz)).date()
            clink=enddate

            params = {
                "action":"TEMPLATE",
                "text":"My Event",
                "dates": f"{clink}/{clink}"
            }
            link = "https://calendar.google.com/calendar/render?" + urlencode(params)
        except Exception as e:
            error = f"unexpected error:{e}"
    return render_template("index.html",dateof=dateof,dayz=dayz,enddate=enddate,link=link)


app.run(debug=True)