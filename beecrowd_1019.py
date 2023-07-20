n = int(input())

try:
    hh = n//3600
    n = n - (hh * 3600)
    mm = n//60
    n = n - (mm * 60)
    ss = n
except:
    pass

print('{}:{}:{}'.format(hh, mm, ss))
