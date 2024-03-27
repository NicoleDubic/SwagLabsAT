Testare automata Swag Labs

Introducere
Acest document conturează planul de testare automatizată pentru Swag Labs, o aplicație web pentru cumpărături.

Obiective
Obiectivele testării automate pentru Swag Labs sunt următoarele:
 - Asigurarea stabilității și fiabilității aplicației Swag Labs.
 - Creșterea vitezei de testare și reducerea efortului manual.
 - Reducerea costului total al testării.
 - Asigurarea că toate produsele adăugate în coș ajung la finalizare.
 - Asigurarea corectitudinii prețurilor.

Amploare
Amploarea testării automate include testarea funcțională a tuturor modulelor.

Instrument de automatizare
Instrumentul de automatizare selectat pentru acest proiect este Selenium versiunea 4.18.1 cu limbajul de programare Python.

Mediu de testare
Mediul de testare pentru testarea automatizată este următorul:
 - Browser: Google Chrome
 - Limbaj de programare: Python
 - IDE: PyCharm

Cazuri de testare
Următoarele cazuri de testare vor fi automatizate:
 - Autentificare în aplicație
 - Sortarea produselor
 - Adăugare produse în coș
 - Vizualizarea detaliilor produsului
 - Finalizarea cumpărăturilor

Date de testare
Următoarele date de testare vor fi utilizate pentru testarea automatizată:
 - Nume de utilizator și parole
 - Informații despre utilizator (Prenume, Nume, Cod poștal)
 - Mesajul de eroare pe care îl așteptăm
 - URL pagina de logare și pagina principală
   
Pentru testare utilizăm locatori (precum: câmpul username, password, burger menu etc.) identificați By.XPATH, By.ID, By.LINK_TEXT.

Execuție testare
Procesul de testare automatizată va urma următorii pași:
 - Identificarea cazurilor de testare ce urmează a fi automate.
 - Dezvoltarea scripturilor de automatizare pentru cazurile de testare identificate.
 - Executarea scripturilor de automatizare.
 - Analizarea rezultatelor testelor.
 - Raportarea execuției.
   
Riscuri și atenuarea impactului acestora
Următoarele riscuri sunt identificate:
 - Schimbări în elementele web: acest lucru poate duce la erori de element ne găsit.
   Pentru a atenua acest risc, localizatorii web vor fi organizați într-un fișier diferit într-un mod dinamic.
 - Modificări ale fluxului de navigare: poate duce la erori de localizare a elementelor, de navigare între pagini, de completare a formularului de facturare.
   Pentru a atenua riscul, se va implementa o practică de revizuire și actualizare regulată a scripturilor de testare automate pentru a le adapta la schimbările în structura paginilor și în fluxul de navigare.
   
Concluzie
Planul de testare automatizată conturează strategia pentru testarea automatizată a aplicației Swag Labs. Acest plan va asigura că aplicația este stabilă și fiabilă. 
Planul va reduce, de asemenea, costul total al testării și va accelera procesul de testare.
