import csv

if __name__=="__main__":
    Employee_Data=[]
    with open("employees.csv","r") as foo:
        Data = csv.DictReader(foo)
        #print(Data)
        for lines in Data:
            if int(lines["SALARY"])>9000:
             phonenumber = lines["PHONE_NUMBER"].split(".")
             phonenumber = "".join(phonenumber)
             Employee_Data.append({"Name":lines["FIRST_NAME"]+" "+lines["LAST_NAME"], "email":lines["EMAIL"],
                                  "phonenumber":lines["PHONE_NUMBER"]})
            else:
                pass
    #print(Employee_Data)
    for i in Employee_Data:
        print(i)


