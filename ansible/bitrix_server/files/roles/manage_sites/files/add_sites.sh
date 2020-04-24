#!/bin/bash

function report {
    echo "Директория сайта: /var/www/$idn
База данных MySQL: $db_name
Логин MySQL: $db_user
Пароль MySQL: $db_pass
Сайт доступен по доменому имени $idn или www.${idn}
"
}

read -p 'Укажите домен: ' domain

idn=$(echo "$domain" | idn)

if [[ "$idn" =~ [[:space:]] ]] || [[ -z "$idn" ]];
then 
    echo "Доменное имя не должно быть пустым и содержать пробелы";
    exit 1
fi

if echo "$idn" | grep -q -E '^w{2,}';
then
    idn=${idn#w*.}
fi

db_pass=$(date +%T | base64)
db_user=$(echo ${idn} | sed -E 's/-|\.//g')
db_name=$db_user

#echo "$idn|$db_pass|$db_user|$db_name"

ansible-playbook -i 'localhost' -e "domain=$idn db_user=$db_user db_name=$db_name db_user_pass=$db_pass" /etc/ansible/roles/manage_sites/tests/test.yml 2>&1 >> /var/log/ansible-playbook.log && report || echo "Произошла ошибка. Подробности в файле /var/log/ansible-playbook.log"
