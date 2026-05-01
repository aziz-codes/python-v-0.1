user = {"age":20,"price":2}
 
result={k:v*v for k,v in user.items() if k=="age"}
print(result)