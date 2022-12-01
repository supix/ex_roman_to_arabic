def convert_roman_to_arabic(roman: str) -> str:
    """
    convert a string containing a number in roman coding to a
    string containing the number in arabic (positinal) coding
    :param roman: string to be converted
    :return: converted string
    """
    # inserisci qui il tuo codice
    """_summary_

    Raises:
        ValueError: Quando nel parametro @roman viene inserito
        un carattere diverso da I , V , X , L , C , D , M 
        restituisce un errore

    Returns:
        _string_: la funzione restituisce la somma dei @Numeri 
        che sono convertiti tramite il dizionario @Roman_Number_Dict

    variables:
        _int_ @Somma : si inizializza a zero e terra traccia della somma dei
        caratteri convertiti
        _int_ @Numero1 e @Numero2 : si inizializzano a zero e il primo indichera 
        il numero corrente mentre il secondo il successivo 
        il corrente deve essere sempre maggiore del successivo per effettuare
        le somme con @Somma in caso contrario tra il numero corrente e @Somma
        verra effettuata la sottrazione 
        _dict_ @Roman_Number_Dict : sara inizializzato con i caratteri romani 
        come chiavi (_string_) e i rispettivi valori (_int_)
        _string_ @Risultato : servira per converitre @Somma _int_ in _string_
    """
    Numero1 = 0
    Numero2 = 0
    Somma = 0
    Roman_Number_Dict = {'I': 1,'V': 5,'X': 10, 'L': 50,'C': 100,'D': 500,'M': 1000}
    
    # Si partira con un ciclo che esamina tutta la stringa roman tranne 
    # lultimo valore, questo perche esso non deve essere confrontato 
    # con il successivo essendo lultimo
    for i in range(len(roman)-1):
        # Si controlla che i caratteri allinterno del carattere corrente 
        # e del successivo siano nel dizionario
        if (roman[i] in Roman_Number_Dict) and (roman[i+1] in Roman_Number_Dict):
            Numero1 = Roman_Number_Dict[roman[i]]
            Numero2 = Roman_Number_Dict[roman[i+1]]
            # Si confrontano i numeri per determinare se bisogna effettuare
            # un'operazione di somma o sottrazione 
            if Numero1 >= Numero2:
                Somma = Somma + Numero1
            else:
                Somma = Somma - Numero1
        else:
            # In caso un carattere di roman non fosse presente nel dict 
            #segnala errore
            raise ValueError
    # si effettueranno le operazioni precedenti ad esclusione del confronto
    if roman[len(roman)-1] in Roman_Number_Dict:
        Somma = Somma + Roman_Number_Dict[roman[len(roman)-1]] 
    else:
        raise ValueError
    # converisone e ritorno del valore   
    Risultato = str(Somma)
    return Risultato