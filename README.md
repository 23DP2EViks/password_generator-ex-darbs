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
Programma tiek palaista caur konsoli un piedāvā 9 izvēlnes punktus. Tālāk ir sniegts detalizēts skaidrojums par to, ko katrs punkts dara un kā to izmantot.

### 1. Ģenerēt paroli
Mērķis: izveidot drošu, unikālu un pielāgojamu paroli.

Kā lietot:

Pēc izvēles ievadiet vajadzīgo paroles garumu (noklusējums: 12 simboli).

Atbildiet uz šādiem jautājumiem (y/n):

Ieslēgt ciparus?

Ieslēgt īpašās rakstzīmes?

Iekļaut arī retās rakstzīmes (piemēram, `[]{}~"`` utt.)?

Norādiet simbolus, ko izslēgt (piemēram: 0OIl|) vai atstājiet tukšu, lai neko neizslēgtu.

Programma ģenerēs paroli, parādīs to un tās stiprumu:
"Vājš", "Vidējs", vai "Spēcīgs".

### 2. Pārbaudīt paroles stiprumu
Mērķis: novērtēt ievadītās paroles drošību.

Kā lietot:

Ievadiet paroli pārbaudei (līdz 128 simboliem).

Programma parādīs tās stiprumu: "Vājš", "Vidējs", vai "Spēcīgs".

Tiks piedāvāts saglabāt šo paroli failā passwords.json (neobligāti).

### 3. Saglabāt ģenerētās paroles failā
Mērķis: saglabāt visas sesijā ģenerētās paroles failā passwords.json.

Kā lietot:

Atlasiet šo vienumu jebkurā brīdī, lai saglabātu visas līdz šim ģenerētās paroles.

Paroles tiek saglabātas kopā ar to stipruma līmeni.

Ja parole jau atrodas failā, tā netiks atkārtoti saglabāta (dublikāti netiek reģistrēti).

### 4. Notīrīt parole failu
Mērķis: pilnībā izdzēst faila passwords.json saturu.

Kā lietot:

Apstipriniet darbību ar y, ja vēlaties dzēst visu faila saturu.

Visas paroles tiks neatgriezeniski izdzēstas.

### 5. Meklēt paroles pēc fragmenta
Mērķis: atrast paroles, kas satur konkrētu rakstzīmju virkni.

Kā lietot:

Ievadiet meklējamo fragmentu.

Programma parādīs visas paroles no faila, kurās šis fragments ir iekļauts.

### 6. Filtrēt paroles pēc stipruma
Mērķis: parādīt tikai tās paroles, kas atbilst izvēlētajam drošības līmenim.

Kā lietot:

Ievadiet vajadzīgā līmeņa numuru:

1 — Vājš

2 — Vidējs

3 — Spēcīgs

Tiks parādīts saraksts ar visām atbilstošajām parolēm.

### 7. Iziet
Mērķis: pārtraukt programmas darbību.

Kā lietot:

Atlasiet šo vienumu, lai izietu no programmas.

### 8. Kārtot paroles un parādīt tabulā
Mērķis: kārtot paroles pēc izvēlēta kritērija un parādīt tabulā ar stipruma norādi.

Kā lietot:

Izvēlieties kārtošanas veidu:

1 — pēc garuma

2 — pēc alfabēta

3 — pēc stipruma

Tiks parādīta tabula ar kolonnām Nr, Parole, Stiprums.

### 9. Rādīt statistiku parolēm
Mērķis: parādīt statistiku par visām saglabātajām parolēm failā.

Kā lietot:

Programma parādīs kopējo paroļu skaitu un sadalījumu pēc līmeņiem:

Cik vājas

Cik vidējas

Cik spēcīgas

## Izmantotās tehnoloģijas

- **Valoda:** Python 3
- **Bibliotēkas:** random, string, json, re.
- **Datu glabāšana:** JSON formātā (`passwords.json`)

## Lietošana

1. Pārliecinies, ka Python 3 ir uzstādīts.
2. Lejupielādē `parolu_generators_un_parvaldnieks.py` failu.
3. Palaid programmu komandrindā.
