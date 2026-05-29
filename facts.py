import urllib.request
import json

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())
    print(f"\n🧠 Random fact:\n{data['text']}\n")
