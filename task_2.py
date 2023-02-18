import csv
import datetime

if __name__=="__main__":
    Employee_Data=[]
    with open("employees.csv","r") as foo:
        Data = csv.DictReader(foo)
        #print(Data)
        for lines in Data:
            if 30<= int(lines["DEPARTMENT_ID"])<110 and int(lines["SALARY"])>4200:
                Date = datetime.datetime.strptime(lines["HIRE_DATE"], "%y-%b-%d")
                #print(Date)
                Date1 = Date.strftime("%Y-%m-%d")
                #print(Date1)
                phonenumber = lines["PHONE_NUMBER"].split(",")
                phonenumber = "".join(phonenumber)
                Employee_Data.append({Date1:lines["FIRST_NAME"]+" "+lines["LAST_NAME"]})
            else:
                pass
    #print(Employee_Data)
    for i in Employee_Data:
        print(i)