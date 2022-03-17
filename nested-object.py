import json

obj = '{"a":{"b":{"c":"d"}}}'
#obj = '{"x":{"y":{"z":"a"}}}'

# convert into JSON:
jsobj = json.loads(obj)


#Recursive function
def find_value(js, findkey):
  if isinstance(js, dict):
    for key, value in js.items():
      if key == findkey:
        print(value)
      else:
        find_value(value, findkey)
  else:
    print("value not found for", findkey)
            

find_value(jsobj, "a")
