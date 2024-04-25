from flask_restful import Resource
from model import *

class demoAPI(Resource):
    
    def post(self):   #adding or sending data to the backend or database CREATE
        return
    
    def get(self):    #retrieve or get data from a database or a function READ
        return
    
    def put(self):    #used to edit database UPDATE
        return 

    def delete(self):  #deletes   DELETE
        return
    

class API(Resource):
    
    def post(self ,title):   #adding or sending data to the backend or database CREATE
        return title
    
    def get(self):    #retrieve or get data from a database or a function READ
        first3movie = movies.query.limit(3).all()
        jason ={}

        counter =0
        for item in first3movie:

            jason['movie'+str(counter)]= (item.id, item.title, item.rating)
            counter+=1
        
        return jason
    
    def put(self):    #used to edit database UPDATE
        return "you are in put"

    def delete(self):  #deletes   DELETE
        return "ok we got it"
    