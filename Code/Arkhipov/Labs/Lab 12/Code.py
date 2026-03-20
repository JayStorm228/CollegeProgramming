import json
import random as r
from pathlib import Path

# Конфигурации
file_name = "LabData.json"
CWD: Path = Path(__file__).resolve().parent
file_path: Path = CWD / file_name
encoding = "utf-8"

# Генерация файла
FloatList1: list[float] = sorted([round(r.uniform(1, 10), 2) for _ in range(10)])
file_path.write_text(
    json.dumps({"FloatList1": FloatList1}, indent=2), encoding=encoding
)

# Изменение файла
data: dict[str, list[float]] = json.loads(file_path.read_text(encoding=encoding))
FloatList2: list[float] = data["FloatList1"]
FloatList2 = sorted(
    [num for num in FloatList2 if num != max(FloatList2) and num != min(FloatList2)]
)

data["FloatList2"] = FloatList2
file_path.write_text(json.dumps(data, indent=2))

print(
    f"""
Generated list of floats: {', '.join(map(str, FloatList1))}
Max value = {max(FloatList1)} and Min value = {min(FloatList1)} removed
New list of floats: {', '.join(map(str, FloatList2))}
    """.strip()
)
