import json

def switch():
  print(" Press 1 for Add New Registration \n Press 2 for Search Student \n Press 3 for Update Status \n Press 4 for Delete Registration\n Press 5 for show all students")
  option =int(input("Your Choice :"))

  def add():
      def write_json(data, filename="students.json"):
          with open(filename, "w") as f:
              json.dump(data, f, indent=4)

      with open("students.json") as json_File:

          id = str(input("Enter Student ID:"))
          name = str(input("Enter Student Name:"))
          section = str(input("Enter Section:"))
          course = str(input("Enter course with course code:"))
          status = str(input("Enter Registration Status:"))
          data = json.load(json_File)
          temp = data["students"]
          y = {"ID": id, "Name": name, "Section": section, "Course": course, "Status": status}
          temp.append(y)
      write_json(data)


  def show():
      print("-----------------------------------------------")
      with open('students.json',"r") as file:
          json_data = json.load(file)
          temp = json_data["students"]
          for item in temp:
              id = item["ID"]
              name = item["Name"]
              course = item["Course"]
              status = item["Status"]
              section = item["Section"]
              print(f"ID : {id}" )
              print(f"Name : {name}")
              print(f"Sction : {section}")
              print(f"Register Course : {course}")
              print(f"Registration Status : {status}")
              print()


  def search():
      id= str(input("Input Student ID you want to search?:"))
      myjsonfile = open('students.json', 'r')
      jsondata = myjsonfile.read()
      obj = json.loads(jsondata)
      list = obj['students']
      for i in range(len(list)):
          if list[i].get("ID") == id:
              print("ID :", list[i].get("ID"))
              print("Name :", list[i].get("Name"))
              print("Section :", list[i].get("Section"))
              print("Course :", list[i].get("Course"))
              print("Status :", list[i].get("Status"))
              print()


  def update_info():
      show()
      id_update = input("Enter the Student ID You want to Update  :  ")

      with open('students.json', "r") as file:
          json_data = json.load(file)
          temp = json_data["students"]
          for item in temp:
              if id_update == item["ID"]:
                  item["Name"] = str(input("Enter Student Name : "))
                  item["Section"] = str(input("Enter Section : "))
                  item["Course"] = str(input("Enter Course Code : "))
                  item["Status"] = str(input("Enter Registration Status : "))
              open("students.json", "w").write(json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': ')))


  def delete():
      show()
      id_delete = input("Enter the Student ID You want to Delete Registration  :  ")
      obj = json.load(open("students.json"))
      list = obj['students']
      for i in range(len(list)):
          if list[i]["ID"] == id_delete:
              list.pop(i)
              break
      open("students.json","w").write(json.dumps(obj,sort_keys=True, indent= 4, separators=(',',': ')))


  dictionary={
      1:add,
      2:search,
      3:update_info,
      4:delete,
      5:show
  }
  dictionary.get(option)()
switch()