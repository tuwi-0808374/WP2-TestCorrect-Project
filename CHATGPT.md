# Inleiding
In de opdracht die wij dit jaar voor de Teach & Learn company uitvoeren zal (weer) gebruik gemaakt worden van ChatGPT. ChatGPT is een voorbeeld van een LLM, een technisch model dat combinaties van woorden herkent en daarop een "antwoord" kan geven dat bij die combinatie goed past. In de probleemstelling gaf de opdrachtgever aan dat men wil proberen vragen op bepaalde manier te categoriseren, maar dat ze nog niet helemaal zeker zijn van welk LLM en welke vorm van vragen ("prompt") het beste resultaat geeft.

In dit document leggen wij uit hoe je ChatGPT vanuit python code een vraag kunt stellen en geven we wat extra handvaten mee over hoe deze te gebruiken in WP2. 

## Hamer
We moeten wel een kanttekening plaatsen bij onze aanpak. "When all you have is a hammer everything looks like a nail". Om een LLM te gebruiken voor een specifiek doel bereik je een veel beter en efficiënter resultaat als je de LLM traint op data voor dat doel. Daarvoor hebben we echter niet de tijd en de middelen. Met ChatGPT zullen we niet het optimale resultaat bereiken en zullen de kosten hoger zijn, maar het zal wel een goed beeld geven van de mogelijkheden van een LLM voor het categoriseren van vragen. 

## OpenAI
OpenAI is een bedrijf dat zich bezighoudt met AI en machine learning. Via hun python package kun je met hun verschillende modellen communiceren. Bijvoorbeeld modellen voor geluids- of fotoherkenning, maar ook voor tekstgeneratie. Al deze modellen zijn getraind op grote hoeveelheden data en kunnen daardoor goed presteren op verschillende taken. 

# ChatGPT in Python
We gaan dus in eerste instantie aan de slag met ChatGPT, of specifiek met de GPT-3.5 versie van ChatGPT. Deze versie is getraind op interpreteren van tekst en zou dus goed moeten werken voor het categoriseren van vragen. Je bent waarschijnlijk al bekend met ChatGPT via de chatbot (https://chatgpt.com/), maar die kan ons in dit geval niet direct helpen. We moeten namelijk vanuit de code met ChatGPT kunnen praten. Dat gaan we niet doen met de website maar met een Python package: `openai`. Dit package is te installeren via pip:
```bash 
pip install openai
```
Vergeet niet dat we jou in WP2 vragen om te werken met een virtual environment.

## API key
De OpenAI python package maakt contact met een website van ChatGPT die alleen toegankelijk is voor code. Dit noem je ook wel een API (Application Programming Interface - en in WP3 gaan we ook zelf een dergelijke API maken). Gebruik van ChatGPT via de API is **niet** gratis. Daarom is er ook een wachtwoord nodig om de API te gebruiken. Omdat dit een wachtwoord is specifiek om met de API te communiceren noemen we die in praktijk ook wel een "API key".

Wij hebben een credit card aan de API gekoppeld en kunnen jou een API key geven, maar om kosten te besparen (want die komen uit onze eigen zak) willen we je vragen om éérst werkende code te tonen in een sprint demo met een vast antwoord op een vraag. Als dat werkt, dan krijg je van ons de API key. Probeer ook daarna gebruik beperkt te houden. 100 vragen kost ons ongeveer 50 cent en de hele dataset er doorheen jassen is dus al snel een paar tientjes.

## Prompt & vraag
Normaliter geef je ChatGPT één prompt, een vraag of een zin waarop ChatGPT een antwoord moet geven. Dat is in dit project ook het deel waar de T&L company aan wil kunnen sleutelen. Daarom splitsen we die in ons project in twee delen. We leggen ChatGPT eerst uit wat we gaan doen (de prompt) en daarna geven we de vraag die gecategoriseerd moet worden. Dit is een manier om ChatGPT te helpen de vraag beter te begrijpen.

## Resultaat
ChatGPT is heel goed in het maken van menselijke tekst, maar heeft wat begeleiding nodig om een antwoord terug te geven in een manier die voor ons makkelijk is te herleiden naar variabelen die we in onze code kunnen gebruiken. We vragen ChatGPT daarom om het resultaat in JSON weer te geven, een formaat dat we in Python makkelijk kunnen omzetten naar een dictionary. 

## Code voorbeeld
Met bovenstaande componenten kunnen we een vraag stellen aan ChatGPT. Hieronder een voorbeeld van hoe dat eruit ziet in Python:
```python
import json

from openai import OpenAI

api_key = "<jouw_persoonlijke_api_sleutel>"
client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
      model= "gpt-3.5-turbo", 
      messages=[
        # Dit is de prompt, om uitleg mee te geven aan ChatGPT
        {"role": "system", "content":
            """
            Wij zijn vragen aan het categoriseren. Kun je de volgende vraag indelen naar de taxonomie van Bloom? We willen maar
            één categorie per vraag.
            
            Kun je het antwoord geven in een RFC8259 JSON met de volgende opmaak:
            
            {
               "categorie": "Categorie",
               "uitleg": "Uitleg"
            }"""
         },
        # Dit is de vraag die we willen categoriseren
        {"role": "user", "content": "Wat voor soort vogel is de grutto?"}
      ]
    )

raw_content = completion.choices[0].message.content
# raw_content is een string, we zetten die om naar een dictionary
content = json.loads(raw_content)
print(content)
```
## Uitgebreid code voorbeeld
Dit voorbeeld is heel basaal, we hebben daarin een aantal zaken nog niet verwerkt die we wel mee moeten nemen. Wat er nog moet worden toegevoegd: 
- Om te voorkomen dat we onnodig veel kosten maken willen we bij het ontbreken van een API key een vast antwoord terug geven, zodat we wel kunnen testen. 
- Deze code kan niet met fouten omgaan. Als er iets mis gaat, dan stopt de code. We willen dat de code blijft draaien en dat we een foutmelding krijgen.
- In WP2 vragen we je code te splitsen naar modules voor de data en de presentatie ("MVC"). Deze code moet dus in een aparte module komen. Mooi zou zijn als je er ook een klasse omheen kunt maken. 

Als we deze zaken meewegen kom je op de volgende code:
```python
import json
import traceback

from openai import OpenAI

def get_bloom_category(question, prompt, api_key, gpt_model="gpt-3.5-turbo"):
  if not api_key:
    print("No API key given, we are returning a static answer for testing")
    return {
      "categorie": "Onthouden",
      "uitleg": "De vraag vereist het onthouden van feitelijke informatie over de Grutto, zoals zijn classificatie als vogelsoort."
    }

  client = OpenAI(api_key=api_key)
  raw_content = None
  result = None
  try:
    completion = client.chat.completions.create(
      model=gpt_model, # alternatieven zijn gpt-3.5-turbo en gpt-4.0-turbo
      messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": question}
      ]
    )

    if len(completion.choices) > 0:
        raw_content = completion.choices[0].message.content
        content = json.loads(raw_content)
        result = {
          "categorie": content.get("categorie"),
          "uitleg": content.get("uitleg")
        }
  except json.JSONDecodeError as e:
      print(f"Error decoding JSON, raw content: {raw_content}")
  except Exception as e:
      traceback.print_exc()
      print(e)
  finally:
    return result
```

Om deze functie te gebruiken kun je de volgende code gebruiken:
```python
prompt = """
Wij zijn vragen aan het categoriseren. Kun je de volgende vraag indelen naar de taxonomie van Bloom? We willen maar
één categorie per vraag.

Kun je het antwoord geven in een RFC8259 JSON met de volgende opmaak:

{
   "categorie": "Categorie",
   "uitleg": "Uitleg"
}"""

question = "Wat voor soort vogel is de grutto?"

# Test
category = get_bloom_category(question, prompt, api_key=None)
print(category)
```
Nu geven we geen API key en zullen we dus altijd hetzelfde antwoord krijgen. Je kunt deze code in jouw project gebruiken, of zelf een alternatief schrijven. 