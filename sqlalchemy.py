import sqlite3
import os
import pandas as pd
from sqlalchemy import create_engine
# os.chdir("E:\qm_daily_Activity\quotemedia_ranking_model\src")

#changing the d
os.chdir(r'E:\Learning work\Api\Rest_api\src')

db = sqlite3.connect('../res/1.db',timeout=100)
c= db.cursor()
# c.execute('''Drop table company13 ''')
c.execute('''CREATE TABLE t1(company_seq_id text primary key asc,company_name text , company_cik int , company_primary_symbol text ,company_short_name text)''')
data_list = [tuple(data.iloc[x,:]) for x in range(len(data))]
for i in data_list:
    c.execute("insert into t1 values (?,?,?,?,?)",i)
db.commit()
v = c.execute('select * from t1').fetchall()
db.close()


engine2 = create_engine('sqlite:///2.db',echo = True)
engine2.table_names()
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True)
    name = Column(String)
    def __repr__(self):
        return "<user (name = '%s')>",(self.name)
# data1 = pd.read_sql('select * from company13 ',engine2)




from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///sd.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)
meta.create_all(engine)
engine.table_names()
ins_val = students.insert()
ins = students.insert().values(name = 'pankaj',lastname = 'patel')
conn = engine.connect()
c = conn.execute(ins)

conn.execute(ins_val, [{'name':'Rajiv', 'lastname' : 'Khanna'},{'name':'Komal','lastname' : 'Bhandari'},{'name':'Abdul','lastname' : 'Sattar'},{'name':'Priya','lastname' : 'Rajhans'},])
pd.read_sql('select * from students',engine)


# selecting the data from TABLE
s = students.select()
result = conn.execute(s)
#select one val
val_one = result.fetchone() # it fetch the value at index 1 and increase the pointer by one , if we execute again then it will give the value at second index
#select many
val_all = result.fetchall() #it fetch the all value  and increase the pointer by one , if we execute again then it will give empty list because it have nan value at next index
for r in result:
    print(r)
#apply tyhe where condition
s_w = students.select().where(students.c.id==1)
result_w =conn.execute(s_w)
result_w.fetchall()
#we can also create the select object using this method
from sqlalchemy.sql import select
s = select([students])
result = conn.execute(s)

#The text() construct is used to compose a textual statement that is passed to the database mostly unchanged
from sqlalchemy import text
str = text('select * from students')
val_text =  conn.execute(str)
for i in val_text:
    print(i)
# use the between in querry

s = text("select students.name, students.lastname from students where students.name between :x and :y")
conn.execute(s, x = 'A', y = 'L').fetchall()

from sqlalchemy.sql import alias
st = students.alias('s')
s = st.select().where(st.c.id < 5)
rs = engine.execute(s)
#It have default size is 1, if we want to print many values then we need to pass the no. of value that you want to print
rs.fetchmany(2)

# The update() method on target table object constructs equivalent UPDATE SQL expression.
# syntax : table.update().where(conditions).values(SET expressions)
up = students.update().where(students.c.lastname == 'patel' ).values(lastname = 'chu')
conn.execute(up)
conn.execute(students.select()).fetchall()

#The delete operation can be achieved by running delete() method on target table object as given in the following statement −
# syntax : students.delete().where(conditions)

conn.execute(students.delete().where(students.c.lastname == 'patel'))
conn.execute(students.select()).fetchall()

#creating multiple tables
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('sqlite:///college.db', echo=True)
engine.table_names()
meta = MetaData()
con1 = engine.connect()
students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

addresses = Table(
   'addresses', meta,
   Column('id', Integer, primary_key = True),
   Column('st_id', Integer, ForeignKey('students.id')),
   Column('postal_add', String),
   Column('email_add', String))
books = Table('books',meta,Column('id',Integer,primary_key = True),Column('Name',String))
meta.create_all(engine)
con1.execute(students.insert(), [
   {'name':'Ravi', 'lastname':'Kapoor'},
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])

con1.execute(addresses.insert(),[
   {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
   {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
   {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
   {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
   {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
])
con1.execute(books.insert(),[{'id':1,'Name':'ASD'},{'id':2,'Name':'qwert'},{'id':4,'Name':'HYult'}])
con1.execute(books.select()).fetchall()
con1.execute(select([students,books]).where(students.c.id == books.c.id)).fetchall()
con1.execute(select([students,addresses,books]).where((students.c.id == addresses.c.st_id) and (students.c.id == books.c.id))).fetchall()

# Using Multiple Table Updates
#
con1.execute(books.update().values({books.c.Name:'MOM'}).where(students.c.id == books.c.id))

 # SQLite dialect however doesn’t support multiple-table criteria within UPDATE and shows following error −
 # 'NotImplementedError: This backend does not support multiple-table criteria within UPDATE'


# Parameter-Ordered Updates
# SET clause in MySQL is evaluated on a per-value basis and not on per-row basis. For this purpose,
# the preserve_parameter_order is used. Python list of 2-tuples is given as argument to the Update.values() method −
'''stmt = table1.update(preserve_parameter_order = True).\
   values([(table1.c.y, 20), (table1.c.x, table1.c.y + 10)])'''
# The List object is similar to dictionary except that it is ordered. This ensures that the “y” column’s SET clause will render first, then the “x” column’s SET clause.
#


# SQLAlchemy Core - Using Joins
# join(right, onclause = None, isouter = False, full = False)
'''The functions of the parameters mentioned in the above code are as follows −

right − the right side of the join; this is any Table object

onclause − a SQL expression representing the ON clause of the join. If left at None, it attempts to join the two tables based on a foreign key relationship

isouter − if True, renders a LEFT OUTER JOIN, instead of JOIN

full − if True, renders a FULL OUTER JOIN, instead of LEFT OUTER JOIN'''
cn = con1.connect()
j1 = addresses.join(students)
j2 = students.join(addresses,students.c.id == addresses.c.st_id)
cn.execute(select([students]).select_from(j1)).fetchall()

# SQLAlchemy Core - Using Conjunctions
'''Conjunctions are functions in SQLAlchemy module that implement relational operators used in WHERE clause of SQL expressions.
 The operators AND, OR, NOT, etc., are used to form a compound expression combining two individual logical expressions.
  A simple example of using AND in SELECT statement is as follows :
SELECT * from EMPLOYEE WHERE salary>10000 AND age>30
  '''

 '''and_() function:'''
 from sqlalchemy import and_ ,or_,asc,desc,between
 cn.execute(students.select().where(and_(students.c.id <=3 , students.c.name == 'Karan'))).fetchall()
 '''or_() function:'''
 cn.execute(students.select().where(or_(students.c.id <=3 , students.c.name == 'Karan'))).fetchall()
 cn.execute(students.select()).fetchall()
 '''asc() function
It produces an ascending ORDER BY clause. The function takes the column to apply the function as a parameter.'''
cn.execute(students.select().order_by(asc(students.c.name))).fetchall()
'''desc() function
Similarly desc() function produces descending ORDER BY clause as follows −'''
cn.execute(students.select().order_by(desc(students.c.name))).fetchall()
'''between() function
It produces a BETWEEN predicate clause. This is generally used to validate if value of a certain column falls between a range. For example,
 following code selects rows for which id column is between 2 and 4 −
'''
cn.execute(students.select().where(between(students.c.id,2,8))).fetchall()


# -----------------SQLAlchemy Core - Using Functions-------------------
from sqlalchemy.sql import func
# In SQL, now() is a generic function to get the current date and time. Following statements renders the now() function using func −
result = conn.execute(select([func.now()]))
print (result.fetchone())

# On the other hand, count() function which returns number of rows selected from a table, is rendered by following usage of func −
cn.execute(select([func.count(students.c.id)])).fetchall()

# The max() function is implemented by following usage of func from SQLAlchemy which will result in 85, the total maximum marks obtained −
cn.execute(select([func.max(students.c.id)])).fetchall()
#find min value
cn.execute(select([func.min(students.c.id)])).fetchall()
#  find Average
cn.execute(select([func.avg(students.c.id)])).fetchall()


# =========================SQLAlchemy Core - Using Set Operations==========================
'''union()''':
from sqlalchemy.sql import union,union_all,except_,intersect
u1 = union(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
conn.execute(u1).fetchone()
ua = union_all(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
conn.execute(ua).fetchall()
ue = except_(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.postal_add.like('%Pune')))
result = conn.execute(ue)
ints = intersect(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.postal_add.like('%Pune')))
result = conn.execute(ints)
