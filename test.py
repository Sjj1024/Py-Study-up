dict1 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
         '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R'}
st1 = ''
for kay, value in dict1.items():
    st1 += f"{kay},{value}"+'\n'
with open('1.txt', 'w+') as f:
    f.write(st1)
