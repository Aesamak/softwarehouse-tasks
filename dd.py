import requests
response = requests.get('https://api.escuelajs.co/api/v1/products')
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data:", response.status_code)
    exit()  
categories = {product["category"]["name"] for product in data}
seen_ids = set()
for category_name in categories:
    print(f"-------{category_name}---------")
    for product in data:
        category = product["category"]["name"]
        if category == category_name and product["id"] not in seen_ids:
            print(product["id"], product["title"], category)
            seen_ids.add(product["id"])
