import json

#obj = '{"a":{"b":{"c":"d"}}}'
obj = '{"x":{"y":{"z":"a"}},"a":{"b":{"c":"d"}}, "m":"n"}'

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

find_value(jsobj, "z")
