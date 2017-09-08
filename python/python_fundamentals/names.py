# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def printer():
#     for x in range(0, len(students)):
#         print students[x]['first_name'],students[x]['last_name']
# printer()

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printer_then_some():
    for key in users:
        print key
        for x in range(0,len(users[key])):
            fn = users[key][x]['first_name']
            ln = users[key][x]['last_name']
            print str(x+1)+ " - " + fn +" "+ ln + " - " + str(len(fn)+ len(ln))


printer_then_some()
