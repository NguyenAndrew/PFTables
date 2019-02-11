# PFTables

Generate CSV tables with fake data (in Python)

Installation Instructions:

1. Install Python 3 (Python 3.7.2)
2. Install pipenv (pip install pipenv)
3. Run the command: `pipenv shell`
4. Run the command: `pipenv install --dev`

Example Usage:

1. Create input.csv (See https://faker.readthedocs.io/en/master/ for possible commands)

```
"Company","Color"
"company","color_name"
```

2. Run the command: `python python pftables.py 3`


3. You should now see and be able to use output.csv

```
"Company","Color"
"Simon PLC","Sienna"
"Trujillo-White","HotPink"
"Harmon, Brown and Crawford","SlateGray"

```



Dependencies

Dependency | Reason for Using
--- |---
 Pylint | Lints
 Faker | Generates Fake Data