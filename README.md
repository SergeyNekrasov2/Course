# Bank's events and main pages project
## Description
Project was created to display basic information about user's bank transactions such as
number of cards, sum of expenses, stock's market and currencies exchange rate

## Installation
Clone git-repository
```chatinput
https://github.com/RafaelManasyan/Module3_Cource_Work.git
```
## Using
Install requirements:
```chatinput
pip install -r requirements.txt
```
1. Call a function and specify in arguments absolute path to file which you need to analise and date
```
main_list = main_list_func(path, user_date)
```
The same applies to events list:
You need to call a events_list-function with two arguments: date and one of the date diapason
"W" — week, "M" - month, "Y" - year, "ALL" - all time
```chatinput
events_list = events_list(user_date, date_coverage="M")
```
## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).