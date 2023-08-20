inp = input()

d = int(inp[0:2])
m = int(inp[3:])

signos = {
    1: (19, 'capricornio', 'aquario'),
    2: (18, 'aquario', 'peixes'),
    3: (20, 'peixes', 'aries'),
    4: (20, 'aries', 'touro'),
    5: (20, 'touro', 'gemeos'),
    6: (20, 'gemeos', 'cancer'),
    7: (22, 'cancer', 'leao'),
    8: (22, 'leao', 'virgem'),
    9: (22, 'virgem', 'libra'),
    10: (22, 'libra', 'escorpiao'),
    11: (21, 'escorpiao', 'sargitario'),
    12: (21, 'sargitario', 'capricornio')
}

if d <= signos[m][0]:
    print(signos[m][1])
else:
    print(signos[m][2])
