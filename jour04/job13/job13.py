#creation de la fonction length
def length(list):
    count=0
    for i in list:
        count+=1
    return count


#creation de la focntion add_list
def add_list(list, e):
    new_list = list[:] + [e]
    return new_list


    
#creation de la fonction delete_double
def delete_double(list):
    len=length(list)
    new_list=[]
    #on comapare chaque élément avec tout les élément qui les suits
    for i  in range (len-1):
        for j in range (i+1 ,len):
            # c'est la valeur ce répète on le supprime en le remplaçant par None
            if list[i] == list[j]:
                list[j]= None
        
    #supprission des case vide de la liste
    for i in range(len):
        if list[i] != None:
            new_list=add_list(new_list,list[i]) 

    return new_list


#liste         
L = [ 10,20,30,20,10,50,60,40,80,50,40]
print(L)

#appel à la fonction delete_double
print(delete_double(L))