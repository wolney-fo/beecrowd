n = int(input())

v_total = 0
p_dias = []

for _ in range(n):
    valor = float(input())
    v_total += valor
    frutas = [x for x in input().split()]
    p_dias.append(len(frutas))

for i in range(n):
    print('day {}: {} kg'.format(i+1, p_dias[i]))

print('{:.2f} kg by day'.format(sum(p_dias)/n))
print('R$ {:.2f} by day'.format(v_total/n))