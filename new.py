data=[123, "test", {"tes":"ytes", "teths": ["yyehs", {"geghehs":"heh" , "hi":["aes","aes2"]},"73££"]}, ["yhwhs","hshe"]]
data2=123
data3="Gaghs"
data4=test_data = {
    "name": "Alice",
    "age": 30,
    "details": {
        "address": {
            "city": "Wonderland",
            "zipcode": 12345,
        },
        "hobbies": ["reading", "chess", {"outdoor": ["cycling", "hiking"]}],
    },
    "scores": [100, 95, {"exam": "final", "marks": 98}],
    "active": True,
}




lis1=[]
def checktype(data,lis,kw=''):
    if type(data)is dict:
        for k,v in data.items():
            if type(v)is dict or type(v)is list:
                checktype(v,lis,kw=f"{kw}:{k}" if kw else k)
            else:
                if kw != "":
                    s = f"{kw}:{k}:{v}"
                else:
                    s = f"{k}:{v}"
                lis.append(s)
    elif type(data)is list:
        for da in data:
            if type(da)is dict or type(da)is list:
                checktype(da,lis,kw)
            else:
                if kw != "":
                    s = f"{kw}:{da}"
                else:
                    s=da
                lis.append(s)
    elif type(data)is str or type(data)is int:
        lis.append(data)
    return lis
o=checktype(data4,lis1)
for l in o:
    print(l)  