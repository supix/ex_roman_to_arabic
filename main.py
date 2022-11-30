def convert_roman_to_arabic(roman: str) -> str:
    """
    convert a string containing a number in roman coding to a
    string containing the number in arabic (positinal) coding
    :param roman: string to be converted
    :return: converted string
    """
    
    #creo un dizionario contenente i valori associati ai numeri romani
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #controllo che l'ultimo valore sia un valore valido se lo è lo uso come valore di partenza
    if dict.get(roman[len(roman)-1],-1)==-1:
        raise ValueError 
    else:
        c=dict.get(roman[len(roman)-1])
    
    for i in range(len(roman)-1):
        #controllo che ogni elemento della stringa sia valido
        b=dict.get(roman[i],-1)
        h=dict.get(roman[i+1],-1)
        if b==-1 or h==-1:
            raise ValueError     
        else:
            #se il primo valore (b) è maggiore del secondo (h) allora li sommo altrimenti lo sottraggo
            if b>=h:
                c+=b
            else:
                c-=b    
    return str(c)