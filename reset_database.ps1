Remove-Item -Path db.sqlite3 -Confirm
Remove-Item -Path base\migrations\*initial.py -Confirm
python .\manage.py makemigrations
python .\manage.py migrate