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
Gender(having), Brand, Type, Size(having), Price(possible), Organic(Y/N), Made in USA(Y/N)

Algorithm process: 
select general size   // general size means the common size we use in our database in case of confliction.
in primary_table      // All tables are list below.
on brand, unique size, Gender, Organic, Made in USA

Search brand(target), unique size(target), price, 
in gender_type table 
on general size, price;

display gender, type, unique size, price, brands(target), Organic, Made in USA
```


b. check the size of cloth in a brand.

```sh
Customers provide: Gender, Type, Brand search for, size, Organic(Possible), Made in USA(Possible)

Algorithm process: 
select general size
in primary_table
on brand, unique size, Gender

Search brand, unique size, price, 
in gender_type table 
on general size, price, brand, Organic(Possible), Made in USA(Possible)

display gender, type, unique size, price, brands(target)
```


c. They don't have a certain requirements of brands.
```sh
Customer proved: Gender, Type, Size, Price(Possible), Organic(Possible), Made_in_USA(Possible)
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
Gender, brand_size, actual_height, brand, type, 

2. Boy Top (long sleeve):
Columns:
brand_size, actual_height, brand, Weight, Chest, Sleeve, Price, Organic, Made_in_USA,

3. Boy Top (short)
Columns:
brand_size, actual_height, brand, Weight, Chest, Sleeve, Price, Organic, Made_in_USA

3. Boy Bottom(pants)
Columns:
brand, brand_size, actual_height, Crotch, Waist, Hip, Instream, Ajustable, weight, Price, Organic, Made_in_USA

4. Boy Bottom(short)
Columns:
Brand, brand_size, actual_height, Waist, Hip, Inseam, Ajustable, weight, Price, Organic, Made_in_USA

5. Girl Top (long)
Brand, brand_size, actual_height, weight, Chest, sleeve, sweep, Price, Organic, Made_in_USA

6. Girl Top (Short)
Brand, brand_size, actual_height, weight, Chest, Sleeve, Sweep, Price, Organic, Made_in_USA

7. Girl Bottom (long)
Brand, brand_size, actual_height, weight, Waist, hip, Inseam, Ajustable, Price, Organic, Made_in_USA

8. Girl Bottom (short)
Brand, brand_size, actual_height, weight, Waist, hip, Inseam, Ajustable, Price, Organic, Made_in_USA

9. Girl Dress
Hollow to floor, Bust, Waist, Hips, Sleeve, inseam, Brand, brand_size, actual_height, weight, Price, Organic, Made_in_USA


