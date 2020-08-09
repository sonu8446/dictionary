import json
data=json.load(open("data.json"))
def translate(w):
   w=w.lower()
   if w in data:
      return data[w]
   else:
      print("Word dosn't exist in my dictionary, Please chexk it!")
word = input("enter word:")
print(translate(word))
