import mysql.connector
import logging

logging.basicConfig (filename='assessment_4_1.log',format='%(asctime)s - %(message)s',level=logging.INFO)
db=mysql.connector.connect(host="localhost",username="root",password="root",db="assessment4")
cursor=db.cursor()

cursor.execute("create table if not exists product(id int,product_name text,product_code text,price int)")
cursor.execute("create table if not exists sale(id int,bill_Date date,product_id int,product_quantity int)")


class assessment:
    
    def max_sold(self):
        logging.info ("max sold prodcut from the table")
        cursor.execute("select product_name,product_code,price from (select product_name,product_code,price,rank() over(order by product_quantity)as r from product p join sale s on p.id=s.product_id)as t where r=1")
        a=cursor.fetchall()
        print(a)
        logging.info ("fetching from cursor for max_sold")
        logging.info (a)


    def min_sold(self):
        logging.info ("min sold selecting from the table")
        cursor.execute("select product_name,product_code,price from (select product_name,product_code,price,rnak() over(order by product_quantity desc)as r from product p join sale s on p.id=s.product_id)as t where r=1")
        a = cursor.fetchall ()
        print (a)
        logging.info ("fetching from cursor for min_sold")
        logging.info (a)

    
    def date_check(self):
        try:
            flag=1
            datee=input("enter the billing date: ")
            cursor.execute("select bill_date from sale")
            dates=cursor.fetchall()
            for x in dates:
                if datee==x:
                    flag=0
            if flag==1:
                raise ValueError
            logging.info ("getting date from user for date_check")
            logging.info (datee)
            logging.info ("selecting from table for date_check")
            cursor.execute("select product_name,product_code,price,count(*)as no_of_rows from product p join sale s on p.id=s.product_id where bill_date=%s",(datee,))
            a = cursor.fetchall ()
            print (a)
            logging.info ("fetching from cursor for date_check")
            logging.info (a)
        except ValueError:
            logging.info (" values not proper")
            print("the date does not match with the file")

    def prod_code(self):
        prod_code=input("enter the product_code: ")
        logging.info ("getting the user input for prod_code")
        logging.info (prod_code)
        logging.info ("selecting from table for prod_code")
        cursor.execute("select product_name,product_code,price from product p join sale s on p.id=s.product_id where product_code=%s",(prod_code,))
        a=cursor.fetchall()
        logging.info ("fetching from cursor for prod_code")
        if(len(a))==0:
            print("the product does not exist for prod_code")
            logging.info ("list not found ")
        else:
            print(a)
            logging.info (" product exists")
            logging.info (a)


    def insertion(self):
        try:
            insertion=[4,"lambo","lmgni-420",999999]
            if(len(insertion))!=4:
                raise IOError
            cursor.execute("insert into product(id ,product_name ,product_code ,price)values(%s,%s,%s,%s)",insertion)

            cursor.execute("select * from product")
            logging.info("selecting everything from product for insertion")
            a=cursor.fetchall()
            logging.info("fetching from cursor for insertion")
            print(a)
            logging.info(a)
        except IOError:
            logging.info ("exception to wrong input ")
            print(" the table has 4 records ")



file=open(r"C:\Users\kisho\Desktop\product.csv")
a=file.read().splitlines()
for x in a:
    b=x.split(",")
    # print(b)
    cursor.execute("insert into product(id ,product_name ,product_code ,price)values(%s,%s,%s,%s)",b)
file.close()
filee=open(r"C:\Users\kisho\Desktop\sale.csv")
b=filee.read().splitlines()
for x in b:
    c=x.split(",")
    # print(c)
    cursor.execute("insert into sale(id ,bill_Date ,product_id ,product_quantity)values(%s,%s,%s,%s)",c)
filee.close()

obj1=assessment()
#obj1.insertion()
#obj1.date_check()
obj1.min_sold()
obj1.max_sold()
#obj1.prod_code()


db.commit()
db.close()

"""output"""
""" [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'lambo', 'lmb-420', 999999)]
enter the billing date: 2019-05-10
the date does not match with the file
[('JBL Speakers', 'JBL-100', 18600)]
[('YAMAHA Speakers', 'YHT-1840', 26500)]
enter the product_code: jbl-100
[('JBL Speakers', 'JBL-100', 18600)]"""

#log-file
# 2020-02-21 12:53:45,851 INFO     selecting from table
# 2020-02-21 12:53:45,852 INFO     fetching from cursor
# 2020-02-21 12:55:05,436 INFO     selecting  from product
# 2020-02-21 12:55:05,437 INFO     fetching from cursor
# 2020-02-21 12:55:05,437 INFO     [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'lambo', 'lmb-420', 999999)]
# 2020-02-21 12:55:34,926 INFO     selecting  from product
# 2020-02-21 12:55:34,927 INFO     fetching from cursor
# 2020-02-21 12:55:41,546 INFO     fetching from cursor
# 2020-02-21 12:58:10,335 INFO     selecting everything from product
# 2020-02-21 12:58:10,336 INFO     fetching from cursor
# 2020-02-21 12:58:10,336 INFO     [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'lambo', 'lmb-420', 999999)]
# 2020-02-21 12:58:15,028 INFO     selecting from table
# 2020-02-21 12:58:15,030 INFO     fetching from cursor
# 2020-02-21 12:58:15,030 INFO     [('JBL Speakers', 'JBL-100', 18600)]
# 2020-02-21 12:58:15,030 INFO     selecting from table
# 2020-02-21 12:58:15,031 INFO     fetching from cursor
# 2020-02-21 12:58:15,031 INFO     [('YAMAHA Speakers', 'YHT-1840', 26500)]
# 2020-02-21 13:00:45,837 INFO     selecting everything from product for insertion
# 2020-02-21 13:00:45,839 INFO     fetching from cursor for insertion
# 2020-02-21 13:00:51,757 INFO     selecting from table for min_sold
# 2020-02-21 13:00:51,759 INFO     fetching from cursor for min_sold
# 2020-02-21 13:00:51,759 INFO     [('JBL Speakers', 'JBL-100', 18600)]
# 2020-02-21 13:00:51,759 INFO     selecting from table for max_sold
# 2020-02-21 13:00:51,761 INFO     fetching from cursor for max_sold
# 2020-02-21 13:00:51,761 INFO     [('YAMAHA Speakers', 'YHT-1840', 26500)]
# 2020-02-21 17:12:02,872 INFO     selecting everything from product for insertion
# 2020-02-21 17:12:02,893 INFO     fetching from cursor for insertion
# 2020-02-21 17:12:20,064 INFO     [('JBL Speakers', 'JBL-100', 18600)]
# 2020-02-21 17:12:20,064 INFO     selecting from table for max_sold
# 2020-02-21 17:12:20,065 INFO     fetching from cursor for max_sold
# 2020-02-21 17:12:20,065 INFO     [('YAMAHA Speakers', 'YHT-1840', 26500)]
# 2020-02-21 17:12:27,919 INFO     getting the user input for prod_code
# 2020-02-21 17:12:27,919 INFO     jbl-100
# 2020-02-21 17:12:27,919 INFO     selecting from table for prod_code
# 2020-02-21 17:12:27,920 INFO     fetching from cursor for prod_code
# 2020-02-21 17:12:27,920 INFO      product exists
# 2020-02-21 17:12:27,920 INFO     [('JBL Speakers', 'JBL-100', 18600)]


