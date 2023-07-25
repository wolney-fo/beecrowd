results = []

qty_operations = int(input())

for i in range(qty_operations):
    values = list(input().split())  
        
    try:
        results.append(float(values[0]) / float(values[1]))
    except:
        results.append('divisao impossivel')

for result in results:
    print(result)