# PFTables

Generate CSV tables with fake data (in Python). Can use Faker, custom arrays, or your own custom functions (hooks).

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

Company | Color | Food | 
--- |--- | ---
 company() | color_name() | [Taco's \| Burger"s \| Pizza,s]
 

2. Run the command: `python pftables.py 5` 
    * Number at the end of the command indicates the number of rows you want.
    * This number can be fairly large! 
    * This program has a loading/progress bar with estimated completion time. Be prepared to wait, if set to over 1 million rows or higher.

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

4. Get Creative!

Example Input: input.csv

Company (Faker Example 1/2) | Credit Card Expiration (Faker Example 2/2) | Food (Array Example 1/2) | Drink (Array Example 2/2) | Element (Hooks Example 1/2) | Abode (Hooks Example 2/2)
--- | --- | --- | --- | --- | --- 
company() | credit_card_expire(start=""now"", end=""+10y"", date_format=""%m/%y"") |[Taco's \| Burger""s \| Pizza,s] | [Water \| Coffee \| Milk \| Tea \| Soda \| Lemonade] |{first_custom_function_example()} | {second_custom_function_example(['House', 'Apartment'])}

```
### Custom Functions (Hooks) ###
### Located in pftables.py ####

def first_custom_function_example():
    """ Code Used to Demonstrate Hooks """
    return random.choices(
        population=['Fire', 'Earth', 'Wind', 'Water'],
        weights=[0.4, 0.3, 0.1, 0.2],
        k=1
    )[0]

def second_custom_function_example(choices):
    """ Code Used to Demonostrate Hooks (with parameters) """
    return random.choice(choices)
```
 
Example Result: output.csv

Company (Faker Example 1/2) | Credit Card Expiration (Faker Example 2/2) | Food (Array Example 1/2) | Drink (Array Example 2/2) | Element (Hooks Example 1/2) | Abode (Hooks Example 2/2)
--- | --- | --- | --- | --- | --- 
Campbell Inc | 11/19 | Taco's | Coffee | Fire | Apartment
Clark LLC | 08/26 | Pizza,s | Coffee | Fire | Apartment
Ramirez Ltd | 02/19 | Taco's | Milk | Fire | House
English, Ray and Jones | 12/19 | Taco's | Tea | Fire | Apartment
Johnson, Jackson and Rangel | 09/23 | Taco's | Tea | Wind | House

## Dependencies

Dependency | Reason for Using
--- |---
 Pylint | Linter
 Faker | Generates Fake Data
 tqdm | Creates a Progress Bar
