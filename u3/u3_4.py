def find_popular (liste):
    n = len(liste)
    print(round(n/2.0))
    dict = {}
    #init dict
    for i in liste:
        dict[i] = 0

    #find dublicates
    for i in liste:
        dict[i] = dict[i] + 1
        #test for populare item
        if dict[i] == round(n/2.0):
            return i
    return None

L = [0,2,301,3,2,1,3,0,0,0,0,2,0]
print(find_popular(L))