# Paroļu ģenerators un pārvaldnieks
Šī ir Python konsoles programma, kas palīdz lietotājiem ģenerēt, pārvaldīt un pārbaudīt paroles pielāgojamā un drošā veidā.

## Galvenās iespējas
✅ Ģenerēt drošas paroles ar pielāgotu garumu, cipariem un simboliem

✅ Iespēja iekļaut vai izslēgt retāk sastopamos simbolus (:;~\|[]{}'")

✅ Izvēlēties, kurus simbolus izmantot vai izslēgt (piemēram, nelietot noteiktus simbolus)

✅ Nodrošināta lietotāja ievades validācija (y/n, cipari u.c.)

✅ Pārbaudīt paroļu stiprumu ar regulārām izteiksmēm (vājš / vidējs / spēcīgs)

✅ Saglabāt paroles failā passwords.json kopā ar to stipruma novērtējumu

✅ Saglabāt tikai unikālas paroles (bez dublikātiem)

✅ Notīrīt parole failu pēc lietotāja pieprasījuma

✅ Meklēt paroles pēc noteikta fragmenta

✅ Filtrēt saglabātās paroles pēc stipruma

✅ Kārtot paroles pēc garuma, alfabēta vai stipruma

✅ Parādīt paroles ērtā tabulas formātā konsolē


## 📘 Programmas lietošanas instrukcija
Programma tiek palaista caur konsoli un piedāvā 8 izvēlnes punktus. Tālāk ir sniegts detalizēts skaidrojums par to, ko katrs punkts dara un kā to izmantot.

### 1. Ģenerēt paroli 

Mērķis: izveidojiet drošu, unikālu un pielāgojamu paroli.

Kā lietot:

Pēc vienuma atlasīšanas ievadiet vajadzīgo paroles garumu (noklusējums 12).

Atbildi uz jautājumiem y/n:

Ieslēgt ciparus??

Ieslēgt īpašās rakstzīmes?

Iekļaut arī retās rakstzīmes (piemēram, []{}~" utt.)?

Lūdzu, norādiet izslēdzamās rakstzīmes (ja tādas ir) vai atstājiet lauku tukšu.

Pēc tam tiks ģenerēta parole un tiks parādīts tās stiprums ("Vājš", "Vidējs", "Spēcīgs").

### 2. Pārbaudīt paroles stiprumu

Mērķis: novērtēt ievadītās paroles drošību.

Kā lietot:

Ievadiet paroli, kuru vēlaties pārbaudīt.

Programma parādīs drošības līmeni: "Vājš", "Vidējs" vai "Spēcīgs".

Jums tiks piedāvāts saglabāt ievadīto paroli failā (neobligāti).

### 3. Saglabāt ģenerētās paroles failā
Mērķis: ierakstiet visas ģenerētās paroles failā passwords.json.

Kā lietot:

Atlasiet šo opciju, lai saglabātu visas iepriekš ģenerētās paroles.

Paroles tiek saglabātas kopā ar to stipruma līmeni.

Dublikāti netiek reģistrēti.

### 4. Notīrīt parole failu

Mērķis: pilnībā izdzēsiet faila passwords.json saturu.

Kā lietot:

Programma prasīs apstiprinājumu.

Ja atbildēsit "y", visas paroles tiks dzēstas bez atkopšanas iespējas.

### 5. Meklēt paroles pēc fragmenta
Mērķis: atrast paroles, kas satur noteiktu apakšvirkni.

Kā lietot:

Ievadiet daļu no paroles vai rakstzīmēm, kurām ir jābūt parolē.

Programma izvadīs atbilstību sarakstu no faila passwords.json.

### 6. Filtrēt paroles pēc stipruma
Mērķis: parādīt paroles, kas atbilst atlasītajam drošības līmenim.

Kā lietot:

Ievadiet līmeņa numuru:

1 — Vājš

2 — Vidējs

3 — Spēcīgs

Programma parādīs paroļu sarakstu no faila, kas atbilst šim līmenim.

### 7. Iziet
Mērķis: pārtraukt programmu.

Kā lietot:

Vienkārši atlasiet šo vienumu, lai izietu no programmas.

### 8. Kārtot paroles un parādīt tabulā
Mērķis: kārtojiet paroles pēc garuma, alfabēta vai to stipruma un parādiet tās tabulā ar norādīto stiprumu.

Kā lietot:

Paroles no faila passwords.json tiks sakārtotas pēc garuma, alfabēta vai stipruma.

Ekrānā parādīsies tabula ar divām kolonnām: "Parole" un "Stiprums".

## Izmantotās tehnoloģijas

- **Valoda:** Python 3
- **Bibliotēkas:** random, string, json, re.
- **Datu glabāšana:** JSON formātā (`passwords.json`)

## Lietošana

1. Pārliecinies, ka Python 3 ir uzstādīts.
2. Lejupielādē `parolu_generators_un_parvaldnieks.py` failu.
3. Palaid programmu komandrindā.
