"""3.	Working with 'csv' and 'json' structures.
Имеется файл cars.csv

Используйте библиотеку csv что бы прочитать содержимое файла.
Конвертируйте данные в формат json и сохраните в файл cars.json

Примечания:
•	используйте csv.DictReader
•	используйте json.dump с параметром indent=2
•	используйте контекстный менеджер with для создания файла

Check yourself:
bash$ cat ../task_23/cars.json
[
  {
    "Year": "1997",
    "Make": "Ford",
    "Model": "E350"
  },
  {
    "Year": "2000",
    "Make": "Mercury",
    "Model": "Cougar"
  },
  {
    "Year": "2006",
    "Make": "Dacia",
    "Model": "Logan"
  }
]
"""
import csv
import json

with open("cars.csv", "r") as file, open("cars.json", "w") as file2:
    json.dump([line for line in csv.DictReader(file)], fp=file2, indent=2)
