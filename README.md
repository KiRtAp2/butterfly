# butterfly
Simulacija različnih primerov kaotičnih sistemov

## Kako uporabljati
Program se zažene z ukazom:

`python3 main.py --module ime_modula`

Kjer je ime_modula ime datoteke v configs/ brez končnice, npr. `lorenz`.

### Dodatne možnosti programa:

`--headless`: Poženi modul brez grafičnega vmesnika. Generira datoteko headless.csv, kamor vsakih debug_time (glej nastavitve) izpiše podatke o vseh točkah.

`--time {ms}`: Nastavi čas, trajanja headless načina v milisekundah.

### Nastavitve (settings.json)

`wwidth`: Širina okna v pikslih

`wheight`: Višina okna v pikslih

`debug`: Ali naj se izvaja debug funkcija. Ignoriran v headless načinu

`debug_time`: Čas med izvajanjem debug funkcije v milisekundah.

`trace_time`: Čas med risanjem zaporednih sledi v milisekundah

### Konfiguracija znotraj modula

`dim`: list z 4 elementi, ki pove, kako se notranje koordinate preslikajo na zaslon

`debug(points: list)`: funkcija, ki se pokliče vsakih debug_time milisekund. Uporabno za tiskanje parametrov

`get_start_points()`: funkcija, ki vrne začetne točke

`do_physics(dt: int, points: list)`: poklicana pred risanjem vsake slike. dt je razlika v času med prejšnjim in tem klicem funkcije v milisekundah

`additional_draw(window: pygame.Surface, points: list, translate: func)`: funkcija dovoljuje dodatno slikanje na zaslon, kjer je to potrebno
