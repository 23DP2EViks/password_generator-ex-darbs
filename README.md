# Paroļu ģenerators un pārvaldnieks

Šī ir Python konsoles programma, kas ļauj lietotājiem:

- Ģenerēt pielāgojamas, drošas paroles
- Pārbaudīt esošo paroļu stiprumu
- Saglabāt paroles ar to stipruma novērtējumu
- Apskatīt visus saglabātos ierakstus
- Filtrēt paroles pēc to stipruma (Spēcīga / Vidēja / Vāja)
- Sekot līdzi darbībām ar žurnāla failu

## Funkcionalitāte

1. **Paroles ģenerēšana** – izvēlies garumu un vai iekļaut ciparus un simbolus.
2. **Paroles stipruma pārbaude** – novērtē drošības līmeni: Spēcīga, Vidēja vai Vāja.
3. **Saglabāšana** – paroles tiek saglabātas failā `passwords.json`.
4. **Paroļu skatīšana** – visi saglabātie ieraksti tiek parādīti ar stipruma informāciju.
5. **Filtrēšana** – iespējams atlasīt tikai noteikta līmeņa paroles.


## Izmantotās tehnoloģijas

- **Valoda:** Python 3
- **Bibliotēkas:** `random`, `string`, `json`, `datetime` (iebūvētās)
- **Datu glabāšana:** JSON formātā (`passwords.json`)


## Lietošana

1. Pārliecinies, ka Python 3 ir uzstādīts.
2. Lejupielādē failu un palaiž programmu:
