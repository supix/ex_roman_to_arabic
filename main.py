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
    for i in range(len(roman)):
        if roman[i] in Roman_Number_Dict:
            Numero = Roman_Number_Dict[roman[i]]
            Somma = Somma + Numero
        else:
            raise ValueError
    Risultato = str(Somma)
    return Risultato