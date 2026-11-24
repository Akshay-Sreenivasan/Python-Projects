import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="akshay@mysql",
    database="shop_example")

mycursor=mydb.cursor()
# admin="create table admin(id int primary key auto_increment,username varchar(100),email varchar(100) unique,role enum('staff',manager') not null)"
# usr="create table users(id int primary key auto_increment,name varchar(100),email varchar(100),phone varchar(10))"
# cate="create table category(id int primary key auto_increment,name varchar(100),admin_id int,foreign key(admin_id) references admin(id))"
# crt="create table products(id int primary key auto_increment,name varchar(100),price decimal(50,2),stock int default 0,admin_id int,category_id int,foreign key(admin_id) references admin(id),foreign key(category_id) references category(id))"
# ord="create table orders(id int primary key auto_increment,productname varchar(100),price decimal(50,2),qty int,user_id int,payment enum('upi','cod','card'),foreign key(user_id) references users(id))"
# pay="create table payment (id int primary key auto_increment,method enum('upi','cod','card') not null,order_id int,foreign key (order_id) references orders(id))"

# sql0="insert into admin(username,email,role) values(%s,%s,%s)"
# val0=("Akshay","akshay@gmail.com","manager"),("sadik","sadik@gmail.com","staff"),("amal","amal@gmail.com","staff")

# sql="insert into users(name,email,phone) values(%s,%s,%s)"
# val=("Ajith","ajith@gmail.com","9898989898"),("Lalu","lalu@gmail.com","6565656565"),("Anu","anu@gmail.com","7656565656")

# sql1="insert into category(name,admin_id) values(%s,%s)"
# val1=("Electronics",1),("cloths",1),("shoes",1),("fruits",2),("vegetables",2),("stationary",2)

# sql2="insert into products(name,price,stock,admin_id,category_id) values(%s,%s,%s,%s,%s)"
# val2=("iphone",100000.00,10,1,1),("samsung",100000.00,10,1,1),("Shirts",3299.00,20,1,2),("pants",4199.00,20,1,2),("nike",5999.00,15,1,3),("adidas",6999.00,15,1,3),("apple",100.00,50,2,4),("banana",50.00,50,2,4),("carrot",30.00,50,2,5),("tomato",40.00,50,2,5),("pen",10.00,40,2,6),("pencil",5.00,50,2,6)

# sql3="insert into orders(productname,price,qty,user_id,payment) values(%s,%s,%s,%s,%s)"
# val3=("shirts",3299.00,1,2,"cod"),("pen",10.00,3,1,"upi")

# sql4="insert into payment(method,order_id) values(%s,%s)"
# val4=("cod",1),("upi",2)

# mycursor.execute(admin)
# mycursor.execute(usr)
# mycursor.execute(cate)
# mycursor.execute(crt)
# mycursor.execute(pay)
# mycursor.execute(ord)
# mycursor.executemany(sql0,vql0)
# mycursor.executemany(sql,val)
# mycursor.executemany(sql1,val1)
# mycursor.executemany(sql2,val2)
# mycursor.executemany(sql3,val3)
# mycursor.executemany(sql4,val4)

mydb.commit()

# print("Table created successfully")

# mycursor.execute("show tables")
# mycursor.execute("select * from admin")
# mycursor.execute("select * from users")
# mycursor.execute("select * from category")
# mycursor.execute("select * from products")
# mycursor.execute("select * from orders")
# mycursor.execute("select * from payment")

result=mycursor.fetchall()
for row in result:
    print(row)

mycursor.close()
mydb.close()
print("Database closed")