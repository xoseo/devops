Role Name
=========

Роль создает конфигурационные файлы для httpd, nginx, базу данных, пользователя, директорию в /var/www, копирует файлы для установки Bitrix

Запустить можно так
`ansible-playbook -i 'localhost' -e "domain=mydomain.local db_user=my__user db_name=my_database db_user_pass=qwerty123" /etc/ansible/roles/manage_sites/tests/test.yml`

В каталоге manage_sites/files лежит скрипт-обертка add_sites.sh который при запуске запросит доменное имя и на основе него сформирует названия БД, пользователя и т.д.
В скрипте захардкоржен плейбук, поэтому каталог manage_sites нужно положить в /etc/ansible/roles

Requirements
------------


Role Variables
--------------


Dependencies
------------


Example Playbook
----------------


License
-------


Author Information
------------------


