# Conversione da numero romano a rappresentazione posizionale in base 10 (araba)

Scrivere una funzione che accetta una stringa di caratteri che contiene la rappresentazione romana di un numero e restituisce una stringa di caratteri che contiene la rappresentazione posizionale in base 10 del numero (codifica araba).

La rappresentazione romana utilizza i simboli:
- I che rappresenta il numero 1
- V che rappresenta il numero 5
- X che rappresenta il numero 10
- L che rappresenta il numero 50
- C che rappresenta il numero 100
- D che rappresenta il numero 500
- M che rappresenta il numero 1000

[SNIP]

La funzione deve riconoscere se nella stringa sono presenti caratteri illegali (che non corrispondono a nessuno dei simboli sopra elencati) e, in questo caso, sollevare un'eccezione.

Viene fornito un file contenente una suite di test che verifica la correttezza della conversione in diversi casi possibili e nel caso la stringa contenga caratteri illegali.

Si suggerisce di estendere la soluzione prevedendo una funzione separata che verifica se la stringa è ben formata, cioè verifica le regole sopra descritte. In tal caso devono essere preventivamente aggiunti i test opportuni. Inoltre, la verifica che la stringa non contenga simboli illegali va integrata in tale funzione e deve essere di conseguenza modificato il test corrispondente.