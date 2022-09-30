import requests

def primek(n):
    n = str(n)
    link = 'https://api.opap.gr/draws/v3.0/1100/' + n
    r = requests.get(link, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = r.json()
    winning_list = data["winningNumbers"]["list"]

    counter = 0
    for i in winning_list:
        if (i%2)!=0:
            counter +=1

    return counter


#Μια άλλη προσέγγιση είναι να πάρουμε την έτοιμη λίστα με τους odd numbers από τον οπαπ και να αποφύγουμε τον έλεγχο που πραγματοποιούμε μόνοι μας


