import sqlite3

conn = sqlite3.connect('pidgey.db')
conn.execute('''CREATE TABLE customer(
    cid	INTEGER NOT NULL,
    cname	VARCHAR(250) NOT NULL,
	cmail	VARCHAR(250) NOT NULL,
	cmobile	INTEGER NOT NULL,
	caddress	VARCHAR(250) NOT NULL,
	cpassword	VARCHAR(250) NOT NULL,
	UNIQUE(cmail),
	UNIQUE(cmobile),
	PRIMARY KEY(cid))''')

conn.execute('''CREATE TABLE IF NOT EXISTS "diginadmin" (
	"amail"	VARCHAR(250) NOT NULL,
	"apassword"	VARCHAR(250) NOT NULL,
	PRIMARY KEY("amail"))''');

conn.execute('''CREATE TABLE IF NOT EXISTS "restadmin" (
	"rid"	INTEGER NOT NULL,
	"rname"	VARCHAR(250) NOT NULL,
	"rmail"	VARCHAR(250) NOT NULL,
	"rmobile"	INTEGER NOT NULL,
	"raddress"	VARCHAR(250) NOT NULL,
	"rpassword"	VARCHAR(250) NOT NULL,
	"cid"	INTEGER NOT NULL,
	UNIQUE("rmobile"),
	UNIQUE("rmail"),
	PRIMARY KEY("rid")
	FOREIGN KEY("cid") REFERENCES "customer"("cid"))''');
	
	
conn.execute('''CREATE TABLE IF NOT EXISTS "orders" (
	"ohash"	INTEGER NOT NULL,
	"cid"	INTEGER NOT NULL,
	"rid"	INTEGER NOT NULL,
	"items"	VARCHAR(250) NOT NULL,
	"tprice"	INTEGER NOT NULL,
	"ostatus"	VARCHAR(20) NOT NULL,
	PRIMARY KEY("ohash"),
	FOREIGN KEY("rid") REFERENCES "restadmin"("rid"),
	FOREIGN KEY("cid") REFERENCES "customer"("cid"))''');


conn.execute('''CREATE TABLE IF NOT EXISTS "items" (
	"iid"	INTEGER NOT NULL,
	"iname"	VARCHAR(250) NOT NULL,
	"iprice"	INTEGER NOT NULL,
	"rid"	INTEGER NOT NULL,
	PRIMARY KEY("iid"),
	FOREIGN KEY("rid") REFERENCES "restadmin"("rid"))''');


conn.execute('''INSERT INTO "customer" VALUES 
    (1,'Kishan Singhal','kishan@k.com',7987697244,'ABC colony Gwalior','kishan'),
    (2,'Anjul Ravi Gupta','anjulgupta@gg.com',8770217188,'Q.no-7/8, B.S.F. Academy, Tekanpur','123456'),
    (3,'Giridhari Lal Gupta','girdhari013@gmail.com',9467906174,'ff','girdhari@'),
    (4,'Gourav','g@g.com',1234565432,'gggg','123456'),
    (5,'Gourav','ggg@gg.com',1234565476,'gggg','123456'),
    (6,'Gourav','ggg@ggg.com',1231265476,'gggg','123456'),
    (7,'Gourav','gggg@ggg.com',3331265476,'gggg','123456'),
    (8,'Gourav','ggggg@ggg.com',3331265466,'gggg','123456')''')


conn.execute('''INSERT INTO "diginadmin" VALUES ('harmanteam@04.com','12345')''')


conn.execute('''INSERT INTO "restadmin" VALUES 
    (1,'Paradise','paradise@p.com',8989565689,'Bangalore','para@123',''),
    (2,'Udupi Hotel','udupi@u.com',9623562314,'Jayanagar Bangalore','udupi@123',''),
    (3,'Hotel Harshitha','harshitha@h.com',8756945212,'J P Nagar Bangalore','harshitha@123',''),
    (4,'Meghanas','meghanas@m.com',9564588956,'Hebbal Bangalore','meghana@123','')''')




conn.execute('''INSERT INTO "orders" VALUES 
    (1,1,1,'1,1,2,2,3,3,5,5,6,6,6',531,'accepted'),
    (2,1,2,'7,7,8,8,8,9,9,10',266,'accepted'),
    (3,1,2,'7,7,9,9',170,'pending'),
    (4,3,1,'1,1,1,1,1',125,'pending'),
    (5,1,1,'3,3',20,'pending'),
    (6,1,1,'1,1',50,'pending'),
    (7,1,1,'1,1,2,2,2,3,3,3,3,5',350,'accepted'),
    (8,1,1,'1,1,1,3,3,3,3,3,3,3,5,5,5,5,5,5,5,6,6,6,6,6,6',922,'pending')''')


conn.execute('''INSERT INTO "items" VALUES (1,'Poha',25,1),
    (3,'samosa',15,1),
    (5,'Biryani',100,1),
    (6,'Tea',7,1),
    (7,'idli',15,2),
    (8,'panipuri',20,2),
    (9,'Chowmein',70,2),
    (10,'chana',36,2),
    (11,'water',15,2),
    (12,'dhokla',21,2)''')





conn.commit()