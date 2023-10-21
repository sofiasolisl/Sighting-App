from sighting_app.config.mysqlconnection import connectToMySQL
from sighting_app.models import user 
from flask import flash

class Sighting:
    def __init__(self, data):
        self.id=data['id']
        self.location=data['location']
        self.date=data['date']
        self.quantity=data['quantity']
        self.description=data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_reporter_id=data['user_reporter_id']
        self.users_who_are_skeptical=[]

    @classmethod
    def getAll (cls):
        query="SELECT * FROM sightings;"
        results=connectToMySQL('exam3').query_db(query)
        sightings=[]
        for sighting in results:
            sightings.append(cls(sighting))
        return sightings
        
    @classmethod
    def getId (cls,id):
        query="SELECT * FROM sightings WHERE id = %(id)s"
        data={
            'id':id
        }
        result=connectToMySQL('exam3').query_db(query,data)
        print("Result", result)
        if len(result)>0:
            return cls(result[0])
        else:
            return None
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO sightings (id, location, date, quantity, description, created_at, updated_at, user_reporter_id) VALUES (%(id)s,%(location)s,%(date)s,%(quantity)s,%(description)s, NOW(),NOW(),%(user_reporter_id)s);"
        print(query)
        mysql = connectToMySQL('exam3')
        result = mysql.query_db(query, data)
        data_usuario={'id':data['id']}
        return cls.getId(data_usuario['id'])
    @classmethod
    def edit (cls, data):
        query = 'UPDATE sightings SET location = %(location)s, date=%(date)s, quantity=%(quantity)s, description=%(description)s WHERE id = %(id)s;'
        mysql = connectToMySQL('exam3')
        result = mysql.query_db(query, data)
        return result
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s and user_reporter_id = %(user_reporter_id)s;"
        mysql = connectToMySQL('exam3')
        result = mysql.query_db(query, data)
        return result
    @classmethod
    def getSkepticals(cls):
        query= f"SELECT sighting_id FROM skeptics;"
        results=  connectToMySQL('exam3').query_db( query )
        sightings=[]
        for sighting in results:
            sightings.append(sighting.get('sighting_id'))
        print (sightings)
        return sightings
    @classmethod
    def getAllReportersInfo(cls):
        query='SELECT users.fname,users.lname, user_reporter_id, users.id as user_id, sightings.id as sighting_id FROM sightings LEFT JOIN users ON users.id=user_reporter_id;'
        results=  connectToMySQL('exam3').query_db( query )
        print(results)
        return results
    @classmethod
    def getSightingReporterInfo(cls,sighting_id):
        query=f'SELECT users.fname,users.lname, user_reporter_id, users.id as user_id, sightings.id as sighting_id FROM sightings LEFT JOIN users ON users.id=user_reporter_id WHERE sightings.id={sighting_id};'
        results=  connectToMySQL('exam3').query_db( query )
        print(results)
        return results
    @classmethod
    def getAllSkepticsCount(cls):
        query="SELECT sightings.id as sighting_id ,COUNT(users.id) as count FROM skeptics LEFT JOIN sightings ON sightings.id=skeptics.sighting_id LEFT JOIN users ON users.id=skeptics.user_id GROUP BY sightings.id;"
        results=  connectToMySQL('exam3').query_db( query )
        print(results)
        return results
    @classmethod
    def get_users_skeptical_to_sighting(cls, id):
        query= f"SELECT * FROM users LEFT JOIN skeptics ON skeptics.user_id=users.id LEFT JOIN sightings ON skeptics.sighting_id=sightings.id WHERE sightings.id={id};"
        results=  connectToMySQL('exam3').query_db( query )
        print(type(results))
        if len(results) == 0:
            return "No users skeptical"
        sighting = cls( results[0] )
        for row_from_db in results:
            user_data = {
                "id" : row_from_db["user_id"],
                "fname" : row_from_db["fname"],
                "lname" : row_from_db["lname"],
                "password" : row_from_db["password"],
                "email" : row_from_db["email"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"],
            }
            sighting.users_who_are_skeptical.append(user.User(user_data))
        return sighting
    @staticmethod
    def validations(sighting):
        is_valid=True
        if sighting['date'] == "":
            flash('Date is required')
            is_valid=False
        if int(sighting['quantity'])<1:
            flash('# of sightings is required')
            is_valid=False
        if sighting['quantity'] == "":
            flash('# of sightings is required')
            is_valid=False
        if sighting['location'] == "":
            flash('Location is required')
            is_valid=False
        if sighting['description'] == "":
            flash('Description is required')
            is_valid=False
        return is_valid
