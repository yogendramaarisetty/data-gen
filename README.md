# Data-gen
test data generator

This a console application

## Initial Steps

1. Install python3.7
2. go to ./dataGenerator/src and run the following command

  ```pip install -r requirements.txt```
  
        or
        
  ```py -m pip insatll -r requirements.txt```
  
 ## Running the application
 1. open command prompt in src location
 2. Run this command
 ``` py generator.py```
 
 # Example
 ```
ACCOUNT
Select Input Format for account
OPTIONS:
 [1] Text file
 [2] Generate sequence
 [3] Random numbers
 [4] Custom strings
 [5] SKIP
select SKIP if you have initialized the list
Choose option from above: 1
30454 accounts read
Successfully read the account data

COMPANY
Select Input Format for company
OPTIONS:
 [1] Text file
 [2] Generate sequence
 [3] Random numbers
 [4] Custom strings
 [5] SKIP
select SKIP if you have initialized the list
Choose option from above: 1
30454 companys read
Successfully read the company data
 ```
### choose appropriate options to load the segment data
after all segments are loaded

```
Input submitted successfully

account 30454
company 30454
department 30983
costcenter 35506
businesscenter 1
productline 1
geography 1
icsegment 1
fiscalyear 1
month 12
amount 1

Do you want to continue?
```

the above list shows the number of segments loaded

### In my_custom_script.py you can customize the way that you want it to be generated

 
 
 
