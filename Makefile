mig:
	python3 manage.py makemigrations
	python manage.py migrate


loaddata:
	python3 manage.py loaddata posts comments albums photos todos users





# python manage.py dumpdata --indent 4 apps.Post > posts.json
# python manage.py loaddata posts


# showmig:
#     python3 manage.py showmigrations
#