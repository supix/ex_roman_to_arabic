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
        _type_: la funzione restituisce la somma dei @Numeri 
        che sono convertiti tramite il dizionario @Roman_Number_Dict
    """
    Numero = 0
    Somma = 0
    Roman_Number_Dict = {'I': 1,'V': 5,'X': 10, 'L': 50,'C': 100,'D': 500,'M': 1000}
    for i in range(len(roman)-1):
        if (roman[i] in Roman_Number_Dict) and (roman[i+1] in Roman_Number_Dict):
            Numero1 = Roman_Number_Dict[roman[i]]
            Numero2 = Roman_Number_Dict[roman[i+1]]
            if Numero1 >= Numero2:
                Somma = Somma + Numero1
            else:
                Somma = Somma - Numero1
        else:
            raise ValueError
    if roman[len(roman)-1] in Roman_Number_Dict:
        Somma = Somma + Roman_Number_Dict[roman[len(roman)-1]] 
    else:
        raise ValueError
    Risultato = str(Somma)
    return Risultato