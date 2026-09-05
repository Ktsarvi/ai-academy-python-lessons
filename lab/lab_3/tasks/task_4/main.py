import json
import config

with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(config.settings, f)

with open("settings.json", "r", encoding= "utf-8") as f:
    loaded_settings = json.load(f)

print(loaded_settings)