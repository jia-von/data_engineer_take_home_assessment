# Data Engineer Take Home Assessment
| Name | Jia Then |
| --- | --- |
| Position | Data Engineer |

## Github Repository
For more detailed solutions and commit review, kindly refer to https://github.com/jia-von and I will grant access to me repository.

```bash
git clone https://github.com/jia-von/data_engineer_take_home_assessment.git

cd data_engineer_take_home_assessment
```
### Directory Structure
```
data_engineer_take_home_assessment
|-- architecture
|-- figures (this directory contains figures for documentation purposes)
|-- scripting
    |-- farm_api.json (JSON object file)
    |-- farm_function.py (Python script function)
    |-- scripting_solution_human_readable.md
|-- SQL
    |-- sql_solution_human_readable.md
    |-- sql_solution.sql (SQL queries)
```
## SQL 
All solutions to the SQL assessment are found in directory `SQL`. You may copy and paste queries from `sql_solution.sql` in a PostgreSQL database. 

## Scripting
All solutions for the scripting assessment are found in `scripting` directory. You may test the Python script.
```bash
$ cd scripting

# To run the script farm_function.py
# On Ubuntu you may need to use python3 command
$ python farm_function.py
```
## Architecture
`architecture` directory contains no code therefore no commands or setup required. 

### Quote
>- Modern applications generate a large amount and variety of data, across many systems.
>- This data, if harnessed, can be a strategic and tactical asset.
>- Please speak to the design of a data pipeline that would facilitate getting value from such data.
>- Some elements we would like to hear about include:
>1. Extraction, transformation, loading and integration
>2. Enrichment and extension (semantic layer)
>3. Mitigating risk / single source of truth
>4. Scalability, availability and security
>5. Orchestration / workflow / performance
>6. Monitoring (failure, optimization, etc.)

### Analysis
- In my experience writing technical report (if you are referring to other data scientist and engineers), I wouldn't use the word **tactical asset** to describe data, because it mostly defined for military uses. *relating to or constituting actions carefully planned to gain a specific military end.* Reword: **Enriched data can be important asset...**
- 

# Background Review
## Quote Email and Delaney
>- Part of our technical interview process here at Jobber is that we have candidates submit a solution to the problem attached. The solution is used to help us understand your approach to problem solving, testing, and commenting. Please review and let me know when you can have it completed by!
>- If you could please submit your results using the link below as a .zip file that would be great as well.
>- Once the team has had a chance to review your submission i'll be in touch with feedback and/or next steps!
>- Quote Delaney via phone: The assessment will atleast 2 hours of your time.
### Analysis
- Understand my approach to:
    - problem solving
    - testing,
    - commenting.
- Submit results via `.zip` file, assumption made to submit via zip repository style as used by GitHub.
- Reviewers: No further background information was provided by Delaney in regards to reviewer technical knowledge. Are they extremely technical or are they architect.
    - Assumption made that they have knowledge of backend infrastructure, SQL, and programming.
    - Also assume that they might not even know how to code, so I provided `.pdf` version of my work.
    - I program in JavaScript, Python, and C#. Due to the popularity of Python, it is more likely they know Python to evaluate my work.
- Since the assessment was mentioned that it will take only 2 hours, I did not expect there will be extensive testing such as unit and integration testing, because it requires quite number of hours to test all edge cases. Therefore, I have just inserted one case for Python to reveal the ability of my code to accept dynmamic value.
- Assumption was made that I will just need to produce vanilla codes. Therefore no libraries are used to help improve my queries.
- Should I have asked for further clarification in regards to the work?
    - Yes, but also I take into account that this is a technical assessment for a job and they might have 100 other applicants to work with.
