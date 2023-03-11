**Project_Structure**

HRConnect (Project Workin/Root Directory)

- .gitignore
- employees.csv
- main.py
- README.md
- task_1.py
- task_2.py

- venv

- my_utils
  - init.py
  - csv.py venv


    
HRConnect Project :

Download .csv data from following website - 
https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784 

TASK 1:
Write a program to get details of employees who's salary is > 9000. The output should be in 
following format

{  
"Name": "<first_name last_name>", 
"email": "<email>",  
"phone number": "<phone number without DOT>" 
}

TASK 2:

Write a program to get "HIRE DATE" of employee who's department is within range 30 to 110 
AND who's salary is > 4200. The output should be in following format. 

{  
"<HIRE DATE in YYYY-MM-DD format>": 
[ "<first_name last_name>",..., "<first_name last_name>"],   
}

TASK 3:
Add breakpoint in each program at various places and learn usage of pdb library.
Your project name should be "HRConnect" and project structure should be as follows 
 
``` 
├── HRConnect  (project root) 
│   ├── my_utils  (your custom package) 
│   │   ├── __init__.py 
│   │   ├── csv.py  (csv file related functions) 
├── task_one.py  (entry-point for task 1) 
├── task_two.py  (entry-point for task 2) 
├── README.md  (your documentation on project)
 ```

csv.py file should contain a class somewhat like following 
 
class HandleCSV:    
filename = "<absolute-path-of-downloaded-file-here>" 
 
    @classmethod   

def read_entire_csv(cls):     
with open(cls.filename, "r") as foo:      
return foo.readlines()
 
    @classmethod    
def read_csv_line_by_line(cls):   
with open(cls.filename) as bar:        
yield bar.readline() 
 
# TODO - ADD MORE SUCH METHODS HERE  
# TODO - UNDERSTAND USAGE OF `classmethod` HERE 


# GIT CLONE PRACTICE
