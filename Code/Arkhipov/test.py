import json

# Сериализация (объект → строка)
data = {"name": "Павел", "scores": [95, 87, 92]}
json_str = json.dumps(data)  # → '{"name": "Павел", "scores": [95, 87, 92]}'
json_str = json.dumps(data, indent=2, ensure_ascii=False)  # красиво + кириллица

# Десериализация (строка → объект)
data2 = json.loads(json_str)
