# SQL Assignment
Use SQL to solve this problem. We are evaluating this from the lens that this is your best possible code.

## Problem:
Given Account and Source tables, write SQL scripts to transform:
    1. When an account's utm_name = 'utmcsr', output its utm_value in a column called utm_source
    2. When an account's utm_name = 'utmcmd', output its utm_value in a column called utm_medium

## Setup:
PostgreSQL syntax and snake_case is used as nomenclature for this exercise.
1. PostgreSQL database was deployed locally to recreate the tables provided by Jobber.
2. Create tables 'accounts' and 'sources'. 
3. Insert data into the tables.
4. Create primary and foreign key. Note: No explicit instruction was given in the exercise in regards to making relational database. Therefore an assumption was made based on one to many relationship, from 'accounts' to 'sources'.
5. Create a SQL query that will produce an output similar to 'expected output'. Note: No explicit instruction that I would need to create an 'expected output' table. Therefore, the solution for this exercise is a SQL query. 

## Solution
### Re-create the table named 'accounts' and 'sources'
```sql
CREATE TABLE public.accounts (
	account_id int NULL,
	account_name varchar NULL
);

CREATE TABLE public.sources (
	account_id int NULL,
	utm_name varchar NULL,
	utm_value varchar NULL
);
```

### Insert data into tables. 
```sql
INSERT INTO public.accounts (account_id,account_name)
	VALUES (226,'aaa');
INSERT INTO public.accounts (account_id,account_name)
	VALUES (971,'bbb');
INSERT INTO public.accounts (account_id,account_name)
	VALUES (598,'ccc');
INSERT INTO public.accounts (account_id,account_name)
	VALUES (999,'ddd');

INSERT INTO public.sources (account_id,utm_name,utm_value)
	VALUES (226,'utmcsr','facebook');
INSERT INTO public.sources (account_id,utm_name,utm_value)
	VALUES (226,'utmcmd','cpc');
INSERT INTO public.sources (account_id,utm_name,utm_value)
	VALUES (971,'utmcsr','google');
INSERT INTO public.sources (account_id,utm_name,utm_value)
	VALUES (971,'utmcmd','cpc');
INSERT INTO public.sources (account_id,utm_name,utm_value)
	VALUES (598,'utmcmd','cpc');
INSERT INTO public.sources (account_id,utm_name,utm_value)
	VALUES (598,'utmcsr','google');
INSERT INTO public.sources (account_id,utm_name,utm_value)
	VALUES (999,'utmcsr','twitter');
```
### Add primary and foreign keys. 
```sql
ALTER TABLE public.accounts ADD CONSTRAINT accounts_pk PRIMARY KEY (account_id);

ALTER TABLE public.sources ADD CONSTRAINT sources_fk FOREIGN KEY (account_id) REFERENCES public.accounts(account_id);
```
### SQL queries to re-create 'expected output'
```sql
SELECT DISTINCT account_name, utm_source, utm_medium 
FROM
    (
    SELECT utm_s.account_id, utm_source, utm_medium 
    FROM
        (
        -- When an account's utm_name = 'utmcsr', output its utm_value in a column called utm_source
        -- Alias, 'AS' was used to assign 'utm_value' with temporary name 'utm_source'. Refer: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-column-alias/
        SELECT account_id, utm_value AS utm_source
        FROM sources 
        WHERE utm_name = 'utmcsr'
        ) AS utm_s
        -- Since account with the name account_name 'ddd' or account_id '999' do not have 'utmcmd' row, temporary tables 'utm_s' and 'utm_m' will have none matching rows. 
        -- Therefore, FULL OUTER JOIN was used to set NULL values for every column of the table that does not have the matching row
        -- Refer: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-full-outer-join/
FULL OUTER JOIN 
        (
        -- When an account's utm_name = 'utmcmd', output its utm_value in a column called utm_medium
        SELECT account_id, utm_value AS utm_medium
        FROM sources 
        WHERE utm_name = 'utmcmd'
        ) AS utm_m 
        ON utm_s.account_id = utm_m.account_id
    ) AS exp_out
LEFT JOIN accounts ON exp_out.account_id = accounts.account_id
```

## Screenshot of output
![screen_shot_sql](../figures/screen_shot_sql.png)