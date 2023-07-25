total_distance = int(input())
total_consumption = float(input())

try:
    print('{:.3f} km/l'.format((total_distance / total_consumption)))
except:
    print()