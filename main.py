from flask import Flask , render_template,request,redirect,url_for
from sqlalchemy import text
from sqlalchemy.sql.expression import func
from model import *
from flask_restful import Api
from api import *
import os

#flask will be the backbone

current_dir = os.path.abspath(os.path.dirname(__file__))

#print("os.path.dirname(__file__)==>", os.path.dirname(__file__))

app = Flask(__name__)  
#these are specil variables which gives additional info
#__name__ tells from where we are running the file if we are running it directly it will show
#__main__
#print(__name__)
#print(__file__) this will give the location of the file running

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(current_dir, "database.sqlite3")
#tells where we can find the database that is we know where the plug for 
#charger is but do not connect it



api = Api(app)
api.add_resource(API,'/api/Bootcamp/','/api/Bootcamp/<title>',)


db.init_app(app)
#db comes from modal file
app.app_context().push()
#it tells the state of db to app like a traffic signal 

@app.route("/",methods=['POST','GET'])
def into():
    user_type = request.form.get('userType')

    if user_type == 'user':
        # Redirect to /user if the user is a regular user
        return redirect(url_for('login'))
    elif user_type == 'admin':
        # Redirect to /admin if the user is an admin
        return redirect(url_for('admin'))
    return render_template("into.html")



@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        valueemail=request.form['email']
        valuepassword=request.form['password']
        if users.query.filter(users.email==valueemail and users.password == valuepassword).first():
            return redirect(url_for('home'))
        return redirect(url_for('signup'))       
    return render_template("login.html")

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        valueusername = request.form['username']
        valueemail = request.form['email']
        valuepassword = request.form['password']

        if not users.query.filter(users.email == valueemail).all():
                newuser = users(username=valueusername,email=valueemail,password=valuepassword)
                db.session.add(newuser)
                db.session.commit()
                return redirect(url_for('index'))#use func name for redirect
        return render_template("signup.html", error='This user already exists')
    
    return render_template('signup.html')



@app.route("/home")
def home():
    listofmovies = movies.query.all()
    #firstmovie = movies.query.first()

    #choice = movies.query.filter(movies.title == "Thor").first()
    return render_template("page.html", show = listofmovies) 

    #for movie in listofmovies:
    #    print(movie.id , movie.title, movie.rating, movie.poster)
    #,var = listofmovies) #this links the html page with server
    #return "hello, i am sumit"


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bookings", methods=['POST','GET'])
def bookings():
    if request.method=='POST':
        value=request.form["searchKey"]
        print(value) 
    return render_template("bookings.html")

@app.route("/add")
def add():
    newmovie=movies(title="Don", rating="9", poster="random_link")
    db.session.add(newmovie)
    db.session.commit()
    return "Data was added"

@app.route("/filter", methods=["POST"])
def filter():
    value=request.form['searchKey']
    searchType= request.form['filterOptions']

    if searchType == "title":
        result = movies.query.filter(movies.title.like('%'+value+'%')).all()
    elif searchType == "genre":
        value=value.title()
        result = movies.query.filter(movies.genre.any(type=value)).all()
    elif searchType == "rating":
        result = movies.query.filter(movies.rating.like(value+'%')).all()
   
    return render_template("filter.html",data=result)
    

@app.route("/admin",methods=['POST','GET'])
def admin():
    if request.method == 'POST':
        if request.form['formtype']=='add':
            valuetitle = request.form['title']
            valuerating = request.form['rating']
            valueposter = request.form['poster']

            if movies.query.filter(movies.title == valuetitle).first() == None:
                newdata = movies(title=valuetitle,rating=valuerating,poster=valueposter)
                db.session.add(newdata)
                db.session.commit()
                return "new movie added"
            else:
                return "try adding a new movie"
        elif request.form['formtype']=='delete':
            valuetitle = request.form['title']
            tobedelted= movies.query.filter(movies.title == valuetitle).first()
            if tobedelted:
                db.session.delete(tobedelted)
                db.session.commit()
                return "movie deleted"
            else:
                return "movie does not exist"

    
    return render_template("admin.html")


@app.route("/api")
def Demoapi():
    return render_template("api.html")


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')
