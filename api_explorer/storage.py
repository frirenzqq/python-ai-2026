import json
def down(data):
    with open("api_explorer/results.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2 )

        