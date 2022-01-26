from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])

def Average_main():
     if request.method == "POST":
         resp = request.form
         stud_nm = resp.get('nm')
         a = resp.get('fnum')
         b = resp.get('snum')
         c = resp.get('tnum')
         d = resp.get('fnum')
         e = resp.get('finum')
         a = int(a)
         b = int(b)
         c = int(c)
         d = int(d)
         e = int(e)

         result = ((a+b+c+d+e)/5)

         return render_template("result.html",resp = result,num1 = a,num2 = b,num3 = c,num4 = d, num5 = e,nm = stud_nm)
     else:
         return render_template("input.html")


if __name__ == "  main  ":
    app.run(debug = True)





