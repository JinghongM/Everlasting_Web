# Task lists:
In order to shchedule our tasts, Here is a list about the process to design a web app:
1, Scenario: In what case, what servers should provide to our customers
2. Necessary: what info, what resource we need for those servers.
3. Application: How to design algorithm to implement those server by our resource
4. Data: How should us store our data to increase the working efficiency


##  Scenario, Necessary, application
In this part we would like to have a disscussion about the use cases, information customers would prived to use, and what resource and information we need related to size convertor.

Use case: Here we would like to list all possible scenario we would meet related to the data we have in size convertor google sheet. 
Customer provide: list info we could get from customers.
Algortihm process: how we use the information customers provide us to get the information we would like to display to our customers.
Display: what we should display to customers.

a. Customers already get a cloth of certain brand, and they would like to find the same size cloth from different brands(not a certain brands,need to be suggested by our algortihm.) 
```sh
Customer provide: 
Gender(having), Brand, Type, Size(having), Price(possible)

Algorithm process: 
select general size   // general size means the common size we use in our database in case of confliction.
in primary_table      // All tables are list below.
on brand, unique size, Gender

Search brand(target), unique size(target), price, 
in gender_type table 
on general size, price;

display gender, type, unique size, price, brands(target)
```


b. check the size of cloth in a brand.

```sh
Customers provide: Gender, Type, Brand search for, size, 

Algorithm process: 
select general size
in primary_table
on brand, unique size, Gender

Search brand, unique size, price, 
in gender_type table 
on general size, price, brand;

display gender, type, unique size, price, brands(target)
```


c. They don't have a certain requirements of brands.
```sh
Customer proved: Gender, Type, Size
```

d. They just look around and provide no information
```sh
Alorithm
if there is no history record for this customer:
build a popular list for different kinds of items, 
select items from every type,
display those to customers 

if we have history record for this customer
generate web according to customer's hisory record.

```

## data:
in this part, we would like to list tables for different type of cloth. 
Size convertor: 

1. Primary Table
Columns: 
Gender, Unique height, General height, brand, type, 

2. Boy Top (long sleeve):
Columns:
Unique height, General height, brand, Weight, Chest, Sleeve

3. Boy Top (short)
Columns:
Unique height, General height, brand, Weight, Chest, Sleeve

3. Boy Bottom(pants)
Columns:
brand, Unique height, General height, Crotch, Waist, Hip, Instream, Ajustable, weight, 

4. Boy Bottom(short)
Columns:
Brand, Unique height, General height, Waist, Hip, Inseam, Ajustable, weight

5. Girl Top (long)
Brand, Unique height, General height, weight, Chest, sleeve, sweep

6. Girl Top (Short)
Brand, Unique height, General height, weight, Chest, Sleeve, Sweep

7. Girl Bottom (long)
Brand, Unique height, General height, weight, Waist, hip, Inseam, Ajustable

8. Girl Bottom (short)
Brand, Unique height, General height, weight, Waist, hip, Inseam, Ajustable

9. Girl Dress
Hollow to floor, Bust, Waist, Hips, Sleeve, inseam, Brand, Unique height, General height, weight


