# TestCorrect Project

## Overzicht

Welkom bij het TestCorrect-project! Dit project is een webapplicatie ontwikkeld om redacteuren van Test-Correct te ondersteunen bij het beoordelen van toetsvragen en het verbeteren van AI-prompts. Het doel van deze applicatie is om het werk van redacteuren efficiënter te maken door technologie in te zetten voor het automatisch evalueren van vragen op basis van taxonomieën zoals Bloom en RTTI.

Met behulp van AI, specifiek ChatGPT, kunnen redacteuren toetsvragen beoordelen, scoren en verbeteren. De applicatie biedt daarnaast een gebruikersdashboard voor redacteuren, een admin-dashboard voor beheerders, en functionaliteit voor het importeren en exporteren van gegevens in JSON-formaat.

Belangrijkste kenmerken van de applicatie
Beoordelen van toetsvragen met behulp van AI en taxonomieën (Bloom en RTTI).
Inloggen en persoonlijke dashboards voor redacteuren.
Admin-dashboard voor het beheren van gebruikers en vragen.
JSON-import en export voor het opslaan en delen van gegevens.
Met deze webapplicatie willen we redacteuren helpen om sneller en eenvoudiger toetsvragen te verbeteren en de kwaliteit van toetsen te verhogen.

## Vereisten

### 1. Software en versievereisten
Voor het uitvoeren van dit project zijn de volgende vereisten van toepassing:

- **Python-versie:** 3.x (bij voorkeur minimaal 3.12)
- **Git:** Om de repository te clonen.
- **Flask:** Webtoepassingsframework nodig voor dit project.

### 2. Benodigde Python-packages
De onderstaande Python libraries zijn nodig om de applicatie succesvol te draaien:
- `flask`
- `openai`
- `ollama`

Je kunt deze afhankelijkheden installeren met behulp van het meegeleverde `requirements.txt`-bestand of handmatig (zie de installatiestappen voor meer informatie).

---

## Installatie Stappen

### 1. Clone de repository
Om te beginnen, clonen we de repository naar je lokale machine. Gebruik de volgende opdracht:

```bash
git clone https://github.com/username/testcorrect-project.git
cd testcorrect-project
```

### 2. Maak een virtual environment (venv) aan
Het gebruik van een virtual environment is aanbevolen om afhankelijkheden van dit project afzonderlijk te houden. Je kunt een virtual environment aanmaken via de **command line** of via **PyCharm**. Kies de methode die je wilt gebruiken.

#### Optie 1: Command Line
1. Maak een virtual environment aan:
   ```bash
   python -m venv venv
   ```
2. Activeer de virtual environment:
   - Op Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Op macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

#### Optie 2: PyCharm
1. Open **PyCharm** en open het project.
2. Ga naar:
   ```
   File > Settings > Project: <your_project_name> > Python Interpreter
   ```
3. Klik op het **tandwiel-icoon** en selecteer **Add**.
4. Kies voor **New Environment** en selecteer **Virtualenv**.
5. Klik op **OK** om de omgeving aan te maken en te activeren.

---

### 3. Installeer afhankelijkheden

#### Optie 1: Installeren met `requirements.txt` (Aanbevolen)
Zorg ervoor dat je virtual environment is geactiveerd. Installeer daarna de afhankelijkheden met:
```bash
pip install -r requirements.txt
```

#### Optie 2: Installeren zonder `requirements.txt`
Als je `requirements.txt` niet wilt gebruiken, installeer je de benodigde libraries handmatig:
```bash
pip install flask
pip install openai
pip install ollama
```

---

### 4. Configuratie-informatie
Het project heeft geen speciale configuratie nodig, tenzij expliciet anders vermeld. Als er API-sleutels of instellingen nodig zijn:
1. Maak een `.env`-bestand aan in de hoofdmap van het project.
2. Voeg eventuele vereiste variabelen toe op basis van de projectvereisten, zoals:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

---

### 5. Start de applicatie

#### Methode 1: Via de terminal
1. Navigeer naar de hoofdmap:
   ```bash
   cd wp2-2024-mvc-1d2-undefined-1
   ```
2. Start de applicatie:
   ```bash
   flask run
   ```
De applicatie is toegankelijk via [http://127.0.0.1:5000](http://127.0.0.1:5000).

#### Methode 2: Via PyCharm
1. Open het bestand `app.py` in PyCharm.
2. Klik op de **Run**-knop om het script te starten.

---

# WP2 Starter 

Dit is de starter repository voor WP2 2024. Deze bevat: 
- De [casus](CASUS.md)
- Een uitleg over hoe [ChatGPT te gebruiken in Python code](CHATGPT.md)
- Een lijst met [voorbeeld vragen](questions_extract.json) die we willen categoriseren
- Een SQLite [database](databases%2Fdatabase.db)database met tabellen voor gebruikers, vragen en AI prompts.
- De [database tool](lib%2Fdatabase%2Fdatabase_generator.py) om een nieuwe database mee te genereren. Deze is vrij aan te passen.   
- Een [voorbeeld uitwerking](voorbeeld_uitwerking/app.py) van het meest complexe deel van de opdracht
