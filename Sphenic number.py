# Create a function to determine if a number is a sphenic number or not.
# A sphenic number is a positive integer number that is the exact product of 3 distincts
# prime number. 

from sieve_of_eratosthene import sieve_eratosthene


def is_phenic(nb, list_nb_premier):
    """
    This function take the number to test (nb) and the list of prime number determine with
    the sieve of eratosthene. It returns the boolean check, that take the value true if 
    the number is sphenic, and the multiplicators that corresponds to the number
    """
    # mult to store all the divisor
    mult = []

    # at the end, check take the value true if nb is sphenic
    check = False

# Every prime number divisor is add 
    for i in range (1, nb+1):
        if nb%i == 0 and i in list_nb_premier:
            mult.append(i)
# Creation of every triad of divisors
    list_triad = []
    for x in mult:
        for y in mult:
            for z in mult:
                if [x, y, z] not in list_triad and x !=y and y != z and x != z:
                    list_triad.append([x, y, z])
# This loop serve to keep only one triad of a same combination
# To do that, remove the triad if the product of the elements
# is present on another triad
    for elem in list_triad:
        product = elem[0] *  elem[1] * elem[2]
        for s_elem in list_triad:
            if s_elem[0] *  s_elem[1] * s_elem[2] == product:
                list_triad.remove(s_elem)

# For each triad, if the product is equal to the number, then it is a sphenic number
    for triad in list_triad:
        if triad[0] * triad [1] * triad[2] == nb:
            check = True
    return check, mult


# Input of the number to test
nb = int(input("Input the number needed to be tested : "))

# create the list of prime number with the sieve of eratosthene
list_nb_premier = sieve_eratosthene(nb)

# Check corresponds to True if the number is sphenic.
# Div correspond to the multiplicater that give the number
check, mult = is_phenic(nb, list_nb_premier)

if check:
    print(f"The number {nb} is sphenic. Multiplicators are {mult[0]}, {mult[1]} et {mult[2]}.")
else:
    print(f"The number {nb} is not sphenic.")

