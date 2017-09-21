# Here is some experience about MySQL database;

## 1.how to show all the users? 
```sh
mysql> select * from mysql.user;
mysql> select User, Host from mysql.user;
```

## 2. How to drop user 
After select User, Host, we can find a clear table about users and hosts. Then we can use command below.
```sh
mysql> drop user 'everlasting'@'localhost';
```

## 3.Create users;
This is something I copy paste from a tutorial, Just give us some basic idea about how to register a user on MySQL database.
```sh
root@host# mysql -u root -p
Enter password:*******
mysql> use mysql;
Database changed

mysql> INSERT INTO user 
          (host, user, password, 
           select_priv, insert_priv, update_priv) 
           VALUES ('localhost', 'guest', 
           PASSWORD('guest123'), 'Y', 'Y', 'Y');
Query OK, 1 row affected (0.20 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 1 row affected (0.01 sec)

mysql> SELECT host, user, password FROM user WHERE user = 'guest';
+-----------+---------+------------------+
|    host   |   user  |     password     |    
+-----------+---------+------------------+
| localhost |  guest  | 6f8c114b58f2ce9e |
+-----------+---------+------------------+
1 row in set (0.00 sec)
```