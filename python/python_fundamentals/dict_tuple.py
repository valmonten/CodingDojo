# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def dict_to_tuple_list(di):
    li=[]
    for key in di:
        li.append((key,di[key]))
    print li
dict_to_tuple_list(my_dict)