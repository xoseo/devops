### bitrix_server
=========
##### Description
-----------------

Роль создает все необходимое окружение для **CMS Bitrix**. 
Компоненты:
* nginx
* httpd
* php-fpm
* mariadb
* push-server
* memcached
* redis
* Дополнительное ПО для прохождения проверок Bitrix

##### Role Variables
--------------

###### PHP
В переменной **php_version** хранится версия php которая будет установлена на сервере. Пакеты ставятся из репозитория remi. 
Доступны версии: 
* 5.4 
* 5.5 
* 5.6 
* 7.0 
* 7.1 
* 7.2 
* 7.3 
* 7.4

В списке **php_packages** можно указать дополнительные расширения php.

###### MariaDB
**mariadb_user** - пользователь который будет создан при накатывании роли
**mariadb_user_pass** - пароль для этого пользователя
**mariadb_db** - база данных


##### Example Playbook
----------------

Для тестирования роли создайте файл inventory, например:
```
[all]
node1.example.com
```

Далее создайте yml файл следующего содежания:
```
---
- hosts: node1.example.com
  remote_user: root
  roles:
    - bitrix_server
```

###### Запуск установки

`ansible-playbook -i inventory file.yml`

P.S. **Не забудьте закинуть свой ключ на сервер**

##### После того как роль установлена
-------
После того как **ansible** отработает, установка Bitrix доступна по URL которое получается из значения **{{ ansible_facts['nodename'] }}** + **bitrixsetup.php**
В контексте хостинга TimeWeb это URL вида **vdsid-yourlogin.tmweb.ru/bitrixsetup.php**

Чтобы Bitrix проходил все проверки необходимо после установки CMS сделать:
1. В настройках главного модуля включить:
  * Быстрая отдача файлов через Nginx
2. В списке модулей удалить:
  * Компрессия (compression)
3. В настройках модуля Push and Pull указать:
  * Использовать "Push server": Использовать сервер, установленный локально
  * На сервер установлена: Виртуальная машина 7.1 - 7.2 (Bitrix Push server 1.0) 
  * Путь для публикации команд: http://vdsid-yourlogin.tmweb.ru:8895/bitrix/pub/
  * Код-подпись для взаимодействия с сервером: XLvTWBqXoljM7jQ3IJ3hRk2528RswYePcpdDT2hrV7Uzj5Ugnhofw14oX01HMu32ebnMVfEztQQwEK3nFeJC01IZxDi1T11ioDBWgNKMNO8FFZAiQ6KfvQNgzlY0kq4Q
  * Путь для чтения команд (HTTP): http://#DOMAIN#:8893/bitrix/sub/
  * (Websocket) Путь для чтения команд (HTTP): ws://#DOMAIN#:8893/bitrix/subws/
4. Запустить на сервере процессы push-server
  * systemctl start push-server-multi


##### License
-------

Free

##### Author Information
------------------

Kobylkin Konstantin. EPAM DevOps Winter 2019
