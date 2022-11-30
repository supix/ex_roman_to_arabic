def convert_roman_to_arabic(roman: str) -> str:
    """
    convert a string containing a number in roman coding to a
    string containing the number in arabic (positinal) coding
    :param roman: string to be converted
    :return: converted string
    """
    
    #creo un dizionario contenente i valori associati ai numeri romani
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    c=0;
    
    for i in range(len(roman)):
        #controllo che ogni elemento della stringa sia valido
        b=dict.get(roman[i],-1)
        if b==-1:
            raise ValueError        
        else:
            #somma il valore della stringa con quello precedente
            c+=b
    return str(c)