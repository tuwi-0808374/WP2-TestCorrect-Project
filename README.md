# TestCorrect Project

## Overzicht

Het TestCorrect Project is een applicatie die gebruik maakt van Python en verschillende libraries, zoals Flask en OpenAI, om complexe taken te ondersteunen. Volg deze handleiding om het project succesvol te installeren en te draaien.

---

## Vereisten

Voor dit project zijn de volgende vereisten nodig:

- **Python versie:** 3.x (bij voorkeur minimaal 3.12)
- **Benodigde packages:**
  - Flask
  - OpenAI
  - Ollama

Om de benodigde packages te installeren, gebruik je een `requirements.txt`-bestand dat bij dit project is meegeleverd.

---

## Installatie Stappen

Volg onderstaande stappen om het project lokaal te installeren en draaien:

### 1. Clone de repository
Gebruik de volgende opdracht om de repository te clonen naar je lokale machine:

```bash
git clone https://github.com/username/testcorrect-project.git
```

### 2. Maak een virtual environment aan
Het gebruik van een virtual environment wordt aanbevolen om afhankelijkheden voor dit project te isoleren van andere projecten op je machine.

1. Open **PyCharm** (of een ander IDE naar keuze) en open het project.
2. Navigeer naar:
   ```
   File > Settings > Project: <your_project_name> > Python Interpreter
   ```
3. Klik op het tandwiel-icoon en selecteer **Add**.
4. Kies voor **New Environment** en selecteer **Virtualenv**.
5. Klik op **OK** om de omgeving aan te maken.

### 3. Installeer afhankelijkheden
Installeer de benodigde packages door de onderstaande opdracht uit te voeren in de terminal (zorg ervoor dat je virtual environment geactiveerd is):

```bash
pip install -r requirements.txt
```

### 4. Start de applicatie
Gebruik één van de volgende methoden om de applicatie te starten:

#### Methode 1: Via de terminal
Navigeer naar de projectmap en voer de volgende commando's uit:

```bash
cd wp2-2024-mvc-1d2-undefined-1
flask run
```

De applicatie is nu toegankelijk via [http://127.0.0.1:5000](http://127.0.0.1:5000).

#### Methode 2: Via PyCharm
1. Open het bestand `app.py` in PyCharm.
2. Klik op de **Run**-knop om het script uit te voeren.

---

# WP2 Starter 

Dit is de starter repository voor WP2 2024. Deze bevat: 
- De [casus](CASUS.md)
- Een uitleg over hoe [ChatGPT te gebruiken in Python code](CHATGPT.md)
- Een lijst met [voorbeeld vragen](questions_extract.json) die we willen categoriseren
- Een SQLite [database](databases%2Fdatabase.db)database met tabellen voor gebruikers, vragen en AI prompts.
- De [database tool](lib%2Fdatabase%2Fdatabase_generator.py) om een nieuwe database mee te genereren. Deze is vrij aan te passen.   
- Een [voorbeeld uitwerking](voorbeeld_uitwerking/app.py) van het meest complexe deel van de opdracht