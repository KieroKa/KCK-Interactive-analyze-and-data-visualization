import csv
import matplotlib.pyplot as plt

suma = 0
i = 2
liczba_kolumn = 2
'''Puste listy na dane z plików'''
cel2y = []
cel2x = []
cel2n = []

cel2rsy = []
cel2rsx = []
cel2rsn = []

cely = []
celx = []
celn = []

celrsy = []
celrsx = []
celrsn = []

rsely = []
rselx = []
rseln = []

'''Wczytywanie danych'''
liczba_wierszy = sum(1 for row in csv.reader(open('2cel.csv')))
with open('2cel.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        cel2x.append(int(row[1])/1000)
        for liczba_kolumn in range(2, (len(row))):
            suma = suma + float(row[liczba_kolumn])*100
            if i == liczba_wierszy:
                cel2n.append(float(row[liczba_kolumn])*100)
        i = i+1
        suma = suma/(liczba_kolumn-1)
        cel2y.append(suma)
        suma = 0
    i = 2

liczba_wierszy = sum(1 for row in csv.reader(open('2cel-rs.csv')))
with open('2cel-rs.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        cel2rsx.append(int(row[1])/1000)
        for liczba_kolumn in range(2, (len(row))):
            suma = suma+float(row[liczba_kolumn])*100
            if i == liczba_wierszy:
                cel2rsn.append(float(row[liczba_kolumn]) * 100)
        i = i + 1
        suma = suma/(liczba_kolumn-1)
        cel2rsy.append(suma)
        suma = 0
    i = 2
liczba_wierszy = sum(1 for row in csv.reader(open('cel.csv')))
with open('cel.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        celx.append(int(row[1])/1000)
        for liczba_kolumn in range(2, (len(row))):
            suma = suma+float(row[liczba_kolumn])*100
            if i == liczba_wierszy:
                celn.append(float(row[liczba_kolumn]) * 100)
        i = i + 1
        suma = suma/(liczba_kolumn-1)
        cely.append(suma)
        suma = 0
    i = 2

liczba_wierszy = sum(1 for row in csv.reader(open('cel-rs.csv')))
with open('cel-rs.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        celrsx.append(int(row[1])/1000)
        for liczba_kolumn in range(2, (len(row))):
            suma = suma+float(row[liczba_kolumn])*100
            if i == liczba_wierszy:
                celrsn.append(float(row[liczba_kolumn]) * 100)
        i = i + 1
        suma = suma/(liczba_kolumn-1)
        celrsy.append(suma)
        suma = 0
    i = 2

liczba_wierszy = sum(1 for row in csv.reader(open('rsel.csv')))
with open('rsel.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        rselx.append(int(row[1])/1000)
        for liczba_kolumn in range(2, (len(row))):
            suma = suma+float(row[liczba_kolumn])*100
            if i == liczba_wierszy:
                rseln.append(float(row[liczba_kolumn]) * 100)
        i = i + 1
        suma = suma/(liczba_kolumn-1)
        rsely.append(suma)
        suma = 0
    i = 2

"""Tworzenie obrazu o danym rozmiarze"""
fig = plt.figure(figsize=(6.7, 5))
"""Lewa część wykresu"""
ax1 = fig.add_subplot(121)
ax2 = ax1.twiny()  # Tworzenie górnej osi

"""Tworzenie linii wykresu o podanych opcjach"""
ax1.plot(rselx, rsely, 'b', marker='o', markevery=25, markeredgecolor='k', markersize=4.5,
         label='1-Evol-RS', linewidth=0.75)
ax1.plot(celrsx, celrsy, 'g', marker='v', markevery=25, markeredgecolor='k', markersize=4.5,
         label='1-Coev-RS', linewidth=0.75)
ax1.plot(cel2rsx, cel2rsy, 'r', marker='D', markevery=25, markeredgecolor='k', markersize=4.5,
         label='2-Coev-RS', linewidth=0.75)
ax1.plot(celx, cely, 'k', marker='s', markevery=25, markeredgecolor='k', markersize=4.5,
         label='1-Coev', linewidth=0.75)
ax1.plot(cel2x, cel2y, 'm', marker='d', markevery=25, markeredgecolor='k', markersize=4.5,
         label='2-Coev', linewidth=0.75)

legend = ax1.legend(loc='lower right')  # Przeniesienie legendy

"""Opis osi wraz z ograniczeniami i rozmiarami"""
ax1.set_xlabel('Rozegranych gier (x1000)')
ax1.set_xlim(0, 500)
ax1.xaxis.label.set_fontsize(8)

ax1.set_ylabel('Odsetek wygranych gier [%]')
ax1.set_ylim(60, 100)
ax1.yaxis.label.set_fontsize(8)

ax1.tick_params(axis='both', labelsize='8')

"""Opis i ograniczenia górnej osi"""
ax2.set_xlabel('Pokolenie')
ax2.set_xlim([0, 200])
ax2.xaxis.label.set_fontsize(8)
ax2.tick_params(axis='both', labelsize='8')

ax1.grid(linestyle=':')  # Siatka

"""Prawa część wykresu"""
ax3 = fig.add_subplot(122)

data_to_plot = [rseln, celrsn, cel2rsn, celn, cel2n]  # Tworzenie danych do boxplota

ustawsrednia = dict(marker='.', markeredgecolor='black', markerfacecolor='blue', markersize=9)  # Opcje dla średniej
ustawwasy = dict(linestyle='-.')   # Opcje dla wąsów

boxplot = ax3.boxplot(data_to_plot, showmeans=True, meanprops=ustawsrednia, whiskerprops=ustawwasy, notch=True,
                      sym='b+', labels=['1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev'])  # Tworzenie wykresu

for box in (boxplot['boxes']):  # Zmiana koloru dla pudełka
    box.set_color('blue')

for whisker in (boxplot['whiskers']):  # Zmiana koloru dla wąsów
    whisker.set_color('blue')

plt.xticks(rotation=25)  # Ustawienie opisu pod kątem
ax3.xaxis.label.set_size(5)  # Zmiana rozmiaru
ax3.yaxis.tick_right()  # Przeniesienie opisu osi y na prawą stronę
ax3.set_ylim(60, 100)  # Ograniczenia dla osi y
ax3.tick_params(axis='both', labelsize='8')  # Zmiana rozmiaru opisów
ax3.grid(linestyle=':')  # Siatka
plt.show()  # Pokazanie wykresu
plt.savefig('Wykresy.pdf')  # Zapis
plt.close()
