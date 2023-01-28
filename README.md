# pet_project
<h1>Команды</h1>
<b>python manage.py makemigrations</b> - создать файл миграции

<b>python manage.py makemigrations core </b> создать файл миграции
<b>python manage.py migrate</b> - накатить миграции
<b>python ./manage.py runserver</b> - создать суперпользователя
<b>python ./manage.py createsuperuser </b>- создать суперпользователя

создать образ на основе докерфайла <b>docker build . </b>

запустить контейнер <b>docker run -it --name app python  /bin/bash </b>

при ошибке токена -  <b>export DOCKER_BUILDKIT=0</b>  
<b>export COMPOSE_DOCKER_CLI_BUILD=0</b>
