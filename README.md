# Data Engineer Take Home Assessment
This exercise is completed for Data Engineer position at Jobber. 

## Github Repository
For more detailed solutions and commit review, kindly refer to https://github.com/jia-von and I will grant access to me repository. Git knowledge are required to access the information.

## Instructions
This take home assignment has 3 parts: a SQL question, a scripting question and a high-level. Please complete all three questions.

## SQL
Use SQL to solve this problem.
We are evaluating this from the lens that this is your best possible code.

### Description
### Attribution Data
Given Account and Source tables, write SQL scripts to transform:
- 1. When an account's `utm_name` = `utmcsr`, output its `utm_value` in a column called `utm_source`
- 2. When an account's `utm_name` = `utmcmd`, output its `utm_value` in a column called `utm_medium`.

### accounts
| account_id | account_name |
| --- | --- |
| 226 | aaa |
| 971 | bbb |
| 598 | ccc |
| 999 | ddd |

### source
| account id | utm_name | utm_value |
| --- | --- | --- |
| 226 | utmcsr | facebook |
| 226 | utmcmd | cpc |
| 971 | utmcsr | google |
| 971 | utmcmd | cpc |
| 598 | utmcmd | cpc |
| 598 | utmcsr | google |
| 999 | utmcsr | twitter |

### Expected Output
| account_name | utm_source | utm_medium |
| --- | --- | --- |
| aaa | facebook | cpc |
| bbb | google | cpc |
| ccc | google | cpc |
| ddd | twitter |  |