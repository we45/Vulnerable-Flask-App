from faker import Faker
import requests
import time

import os
# fake = Faker()

# for i in range(0,100):
#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     email = fake.email()
#     password = fake.md5(raw_output=False)
#     username = "{0}.{1}".format(first_name, last_name)
#     ccn = fake.credit_card_number(card_type=None)

#     json_val = {"first_name": first_name, "last_name": last_name, "email": email, "password": password, "username": username, "ccn": ccn}

#     resp = requests.post('http://localhost:5050/register/customer', json = json_val)
#     if resp.status_code == '200':
#         print resp.json()

#     time.sleep(2)

mysql_user = os.environ.get('MYSQL_USER', 'root')
mysql_pass = os.environ.get('MYSQL_PASS', 'strongpass')
mysql_host = os.environ.get('MYSQL_HOST', '127.0.0.1')
mysql_db = os.environ.get('MYSQL_DB', 'flasky')

import MySQLdb as mdb

def run_sql_file(filename, connection):
    file = open(filename, 'r')
    sql = s = " ".join(file.readlines())
    print "Start executing: " + filename + "\n" + sql 
    cursor = connection.cursor()
    cursor.execute(sql)        


def main():
    connection = mdb.connect(mysql_host, mysql_user, mysql_pass, mysql_db)
    run_sql_file("/apps/flasky_2017-07-17.sql", connection)
    connection.close()

main()