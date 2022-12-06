# FR
# Le crible d'Ératosthène, ou "sieve of Eratosthene" en anglais,
# est un algorithme permettant de déterminer tous les nombres
# premier inférieurs à une limite. L'idée est que l'on va multiplier
# chaque nombre entier qui n'a pas été marqué, et que chaque fois qu'un nombre
# est multiple d'un, alors il est premier

# ENG
# ToDo

def sieve_eratosthene(limit):
    list_test = []
    p = 2
    dic = {}
    for i in range(2, limit):
        dic[i] = True
    for k in dic.keys():
        p = 2
        if k * k > limit:
            break
        if dic[k]== True:
            while k * p < limit:
                dic[p*k] = False 
                p += 1
    return [elem for elem in dic.keys() if dic[elem] == True]

    