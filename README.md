# PFTables

Generate CSV tables with fake data (in Python). Can use both faker or custom arrays to generate fake data

## Installation Instructions:

1. Install Python 3 (Python 3.7.2)
2. Install pipenv (pip install pipenv)
3. Run the command: `pipenv shell`
4. Run the command: `pipenv install --dev`

## Example Usage

1. Create input.csv (See https://faker.readthedocs.io/en/master/ for available faker functions)

```
"Company","Color", "Food"
"company()","color_name()", "[Taco's | Burger""s | Pizza,s]"
```

Company | Color | Food
--- |--- | ---
 company() | color_name() | [Taco's \| Burger"s \| Pizza,s]
 

2. Run the command: `python python pftables.py 5`


3. You should now see and be able to use output.csv

```
"Company","Color","Food"
"Williams Group","LightSlateGray","Pizza,s"
"Hebert and Sons","Snow","Taco's"
"Ford, Cox and Riley","Lime","Taco's"
"Evans Inc","Orchid","Burger""s"
"Garcia, Rhodes and Willis","NavajoWhite","Pizza,s"

```

Company | Color | Food
--- | --- | ---
Williams Group | LightSlateGray | Pizza,s
Hebert and Sons | Snow | Taco's
Ford, Cox and Riley | Lime | Taco's
Evans Inc | Orchid |Burger"s
Garcia, Rhodes and Willis | NavajoWhite | Pizza,s


## Dependencies

Dependency | Reason for Using
--- |---
 Pylint | Linter
 Faker | Generates Fake Data