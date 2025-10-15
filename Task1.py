def main( ):
    #list1 = [1, 2, 3, 3, 4]
    #list1 = [1, 2, 3, 3, 4, 3]
    #list1 = [1, 2, 3, 3, 8, 4] 
    #list1 = [1, 2, 3, "3", 4]
    list1 = [1, 2, 3, 5, 7, 8, 4]
    list2 = [1, 2, 3, 7, 4, 3] 
    errortext = ''
    for value in list1:
        if list1.count(value) != list2.count(value):
            errortext = errortext  + str(value) + ', '
            #print( "\n" )
            error = True
    else: 
        if not error:
           print('Elements of list1 fully represented in list2')    
        else:
           errortext = errortext[:-2]
           print('Element of list1 "' + errortext  + '" not fully represented in list2') 

main( )