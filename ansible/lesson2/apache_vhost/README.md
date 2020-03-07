apache_vhost
=========

Роль выполняет установку httpd на сервера в группе lamp, создает в каталоге /var/www в директорию с названием полученным из fqdn хоста назначения, копирует туда index.html, открывает порт 80.

Role Variables
--------------

Задана единственная переменна vhosts_configs - путь откуда апач инклюдит конфиги

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: lamp
      roles:
         - apache_vhost

License
-------

Free

Author Information
------------------

Kobylkin Konstantin. EPAM DevOps Winter 2019
