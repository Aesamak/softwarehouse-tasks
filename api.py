import requests

response = requests.get('https://api.escuelajs.co/api/v1/products')
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data:", response.status_code)
i=len(data)
j=0
li=[]
while j<i:
    product=dict(data[j])
    category=product["category"]
    cat_name=category["name"]
    li.append(cat_name)
    res = list(set(li))
    j+=1
print(res)
li2=[]
for h in res:
    print(f"-------{h}---------")
    for product in data:
        category=product["category"] ["name"]
        if product["id"] not in li2 and category==h:
            print(product["id"],product["title"],category)
            li2.append(product["id"])