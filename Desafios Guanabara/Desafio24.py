cidade = input('Digite o nome da sua cidade: ')
s = cidade.upper().split().count('SANTO')
if s == 1:
    print('Sua cidade TEM a palavra SANTO!')
else:
    print('Sua cidade NÂO tema palavra SANTO')
