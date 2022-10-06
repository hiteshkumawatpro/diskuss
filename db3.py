import psycopg2
from django.template.defaultfilters import slugify
def createtable():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("Create table data(Name TEXT, Id INTEGER primary key, Marks INTEGER)")
    conn.commit()
    conn.close()

def droptable():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("drop table data")
    conn.commit()
    conn.close()

def insertData():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute(f"insert into data(Name,Id,Marks) values('A reducing water pipe section has an inlet diameter of 50 mm and exit diameter of 30 mm. If the steady inlet speed (averaged across the inlet area) is 2.5 m/s, find the exit speed. ',1002,98),('‘The air resistance (drag force) on a 200 g ball in free flight is given by Fp = 2x 10~*V?, where Fy is in newtons and V is in meters per second. If the ball is dropped from rest 500 m above the ground, determine the speed at which it hits the ground. What per- centage of the terminal speed is the result? (The terminal speed is the steady speed a falling body eventually attains.) ',1003,75),('Water flows through pipes A and B. Lubricating oil is in the upper portion of the inverted U. Mercury is in the bottom of the manometer bends. Determine the pressure difference, pa—pa, in units of Ibf/in.? ',1004,57),('‘The maximum power output capability of a gasoline or diesel engine decreases with altitude because the air density and hence the mass flow rate of air decreases. A truck leaves Denver (elevation 5280 ft) on a day when the local temperature and barometric pressure are 80°F and 24.8 in, of mercury, respectively. Ittravels through Vail Pass (elevation 10,600 ft), where the temperature is 62°F, Determine the local barometric pressure at Vail Pass and the percent change in density. ',1005,54)")
    conn.commit()
    conn.close()

def displaydata():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("select * from data")
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()


def selectKeyword():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("select Name,Id from data")
    print(cur.fetchall())
    conn.commit()
    conn.close()

def condition():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("select * from data where Id>1004 AND Marks>50")
    print(cur.fetchall())
    conn.commit()
    conn.close()


def update_conditional():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("update data set Marks=200 where Id = 1003")
    conn.commit()
    conn.close()


def delete_row_table():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("delete from data where Id=1001")

    conn.commit()
    conn.close()

def order_by():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("select * from data order by Marks asc")
    print(cur.fetchall())
    conn.commit()
    conn.close()


def createViews():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("create view data2_view as select Name,Id from data")

    conn.commit()
    conn.close()


def display_Views():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("select * from data2_view")
    print(cur.fetchall())
    conn.commit()
    conn.close()




def usefn():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("select fetch_details()")
    k = cur.fetchall()
    print(k)
    conn.commit()
    conn.close()

def creatrtable():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("Create table question_database(question TEXT ,id INTEGER,chapter TEXT)")
    conn.commit()
    conn.close()


def creattable():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("Create table User_Upload_Details(question_id INTEGER primary key,Question_Img_Id Text ,Name TEXT, Message TEXT)")
    conn.commit()
    conn.close()

def inserData():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("insert into question_database(question,id,chapter) values('A piston-cylinder device contains 0.95 kg of oxygen initially at a temperature of 27°C and a pressure due to the weight of 150 kPa (abs). Heat is added to the gas until it reaches a temperature of 627°C. Determine the amount of heat added during ',1101,'Fluids'),('A reducing water pipe section has an inlet diameter of 50 mm and exit diameter of 30 mm. If the steady inlet speed (averaged across the inlet area) is 2.5 m/s, find the exit speed. ',1102,'Fluids'),('‘The air resistance (drag force) on a 200 g ball in free flight is given by Fp = 2x 10~*V?, where Fy is in newtons and V is in meters per second. If the ball is dropped from rest 500 m above the ground, determine the speed at which it hits the ground. What per- centage of the terminal speed is the result? (The terminal speed is the steady speed a falling body eventually attains.) ',1103,'Fluids'),('Water flows through pipes A and B. Lubricating oil is in the upper portion of the inverted U. Mercury is in the bottom of the manometer bends. Determine the pressure difference, pa—pa, in units of Ibf/in.? ',1104,'Fluids'),('‘The maximum power output capability of a gasoline or diesel engine decreases with altitude because the air density and hence the mass flow rate of air decreases. A truck leaves Denver (elevation 5280 ft) on a day when the local temperature and barometric pressure are 80°F and 24.8 in, of mercury, respectively. Ittravels through Vail Pass (elevation 10,600 ft), where the temperature is 62°F, Determine the local barometric pressure at Vail Pass and the percent change in density. ',1105,'Fluids')")

    conn.commit()
    conn.close()

def inData():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("insert into User_Upload_Details(question_id,question_img_id,name,message) values(1101,'1101_1','ram','we used fluids concepts'),(1102,'1102_1','shyam','we used fluids concepts 2'),(1103,'1103_1','mohan','we used fluids concepts 3'),(1104,'1104_1','sohan','we used fluids concepts 4'),(1105,'1105_1','aditya','we used fluids concepts 5')")

    conn.commit()
    conn.close()
inData()