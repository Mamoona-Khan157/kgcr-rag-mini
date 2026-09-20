import spacy
import json

text = (
    "Berners-Lee was born in London on 8 June 1955. "
    "Berners-Lee worked as an independent contractor at CERN "
    "from June to December 1980. While in Geneva, he proposed "
    "a project based on the concept of hypertext, to facilitate "
    "sharing and updating information among researchers."
)

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

entities = []
for ent in doc.ents:
    entities.append({
        "text": ent.text,
        "label": ent.label_
    })

found_texts = {e["text"] for e in entities}
extra_entities = [
    ("8 June 1955", "DATE"),
    ("June to December 1980", "DATE"),
    ("hypertext", "CONCEPT"),
    ("independent contractor", "ROLE"),
    ("researchers", "GROUP"),
    ("project", "ARTIFACT"),
]
for name, label in extra_entities:
    if name not in found_texts:
        entities.append({"text": name, "label": label})

relations = [
    {"head": "Berners-Lee", "relation": "bornIn", "tail": "London"},
    {"head": "Berners-Lee", "relation": "birthDate", "tail": "8 June 1955"},
    {"head": "Berners-Lee", "relation": "workedAt", "tail": "CERN"},
    {"head": "Berners-Lee", "relation": "hadRole", "tail": "independent contractor"},
    {"head": "Berners-Lee", "relation": "workPeriod", "tail": "June to December 1980"},
    {"head": "Berners-Lee", "relation": "locatedIn", "tail": "Geneva"},
    {"head": "Berners-Lee", "relation": "proposed", "tail": "project"},
    {"head": "project", "relation": "basedOn", "tail": "hypertext"},
    {"head": "project", "relation": "purpose", "tail": "sharing and updating information among researchers"},
]

output = {
    "entities": entities,
    "relations": relations
}

with open("outputs.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("Done! outputs.json has been created.")
print(json.dumps(output, indent=2, ensure_ascii=False))