# import pyspark class Row from module sql -demo
from pyspark.sql import *
spark = SparkSession.builder.getOrCreate()
# Create Example Data - Departments and Employees

# Create the Departments
department1 = Row(id='101', name='Computer Science')
department2 = Row(id='102', name='Mechanical Engineering')
department3 = Row(id='103', name='Theater and Drama')
department4 = Row(id='104', name='Indoor Recreation')

# Create the Employees
Employee = Row("firstName", "lastName", "email", "salary","deptId")
employee1 = Employee('michael', 'armbrust', 'no-reply@berkeley.edu', 100000,101)
employee2 = Employee('xiangrui', 'meng', 'no-reply@stanford.edu', 120000,101)
employee3 = Employee('matei', None, 'no-reply@waterloo.edu', 140000,102)
employee4 = Employee(None, 'wendell', 'no-reply@berkeley.edu', 160000,102)
employee5 = Employee('michael', 'jackson', 'no-reply@neverla.nd', 80000,103)
employee6 = Employee('john', 'doe', 'no-reply@unclesame.usa.gov', 800000,101)

depts = [department1, department1,department3,department4]
employees = [employee1, employee2,employee3,employee4,employee5,employee6]

deptsDF = spark.createDataFrame(depts)
empsDF = spark.createDataFrame(employees)

deptsDF.show()
empsDF.show()
