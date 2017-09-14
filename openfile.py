#!/usr/bin/env python3

import sys
import csv

print(sys.path)

usertab=[{'passwrd': 'x', 'shell': '/bin/bash', 'full_name': 'root', 'user_id': '0', 'group_id': '0', 'home_directory': '/root', 'username': 'root'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'daemon', 'user_id': '1', 'group_id': '1', 'home_directory': '/usr/sbin', 'username': 'daemon'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'bin', 'user_id': '2', 'group_id': '2', 'home_directory': '/bin', 'username': 'bin'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'sys', 'user_id': '3', 'group_id': '3', 'home_directory': '/dev', 'username': 'sys'},
{'passwrd': 'x', 'shell': '/bin/sync', 'full_name': 'sync', 'user_id': '65534', 'group_id': '4', 'home_directory': '/bin', 'username': 'sync'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'games', 'user_id': '60', 'group_id': '5', 'home_directory': '/usr/games', 'username': 'games'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'man', 'user_id': '12', 'group_id': '6', 'home_directory': '/var/cache/man', 'username': 'man'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'lp', 'user_id': '7', 'group_id': '7', 'home_directory': '/var/spool/lpd', 'username': 'lp'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'mail', 'user_id': '8', 'group_id': '8', 'home_directory': '/var/mail', 'username': 'mail'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'news', 'user_id': '9', 'group_id': '9', 'home_directory': '/var/spool/news', 'username': 'news'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'uucp', 'user_id': '10', 'group_id': '10', 'home_directory': '/var/spool/uucp', 'username': 'uucp'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'proxy', 'user_id': '13', 'group_id': '13', 'home_directory': '/bin', 'username': 'proxy'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'www-data', 'user_id': '33', 'group_id': '33', 'home_directory': '/var/www', 'username': 'www-data'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'backup', 'user_id': '34', 'group_id': '34', 'home_directory': '/var/backups', 'username': 'backup'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'Mailing List Manager', 'user_id': '38', 'group_id': '38', 'home_directory': '/var/list', 'username': 'list'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'ircd', 'user_id': '39', 'group_id': '39', 'home_directory': '/var/run/ircd', 'username': 'irc'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'Gnats Bug-Reporting System (admin)', 'user_id': '41', 'group_id': '41', 'home_directory': '/var/lib/gnats', 'username': 'gnats'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': 'nobody', 'user_id': '65534', 'group_id': '65534', 'home_directory': '/nonexistent', 'username': 'nobody'},
{'passwrd': 'x', 'shell': '', 'full_name': '', 'user_id': '101', 'group_id': '100', 'home_directory': '/var/lib/libuuid', 'username': 'libuuid'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '104', 'group_id': '101', 'home_directory': '/home/syslog', 'username': 'syslog'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '105', 'group_id': '102', 'home_directory': '/var/run/dbus', 'username': 'messagebus'},
{'passwrd': 'x', 'shell': '/usr/sbin/nologin', 'full_name': '', 'user_id': '65534', 'group_id': '103', 'home_directory': '/var/run/sshd', 'username': 'sshd'},
{'passwrd': 'x', 'shell': '/bin/zsh', 'full_name': '', 'user_id': '1000', 'group_id': '1000', 'home_directory': '/home/maddeer', 'username': 'maddeer'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '111', 'group_id': '104', 'home_directory': '/var/cache/bind', 'username': 'bind'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': 'MySQL Server,,,', 'user_id': '112', 'group_id': '105', 'home_directory': '/nonexistent', 'username': 'mysql'},
{'passwrd': 'x', 'shell': '/bin/bash', 'full_name': ',,,', 'user_id': '1001', 'group_id': '1001', 'home_directory': '/home/homeip', 'username': 'homeip'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '65534', 'group_id': '106', 'home_directory': '/var/lib/fetchmail', 'username': 'fetchmail'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '114', 'group_id': '107', 'home_directory': '/var/spool/postfix', 'username': 'postfix'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': 'Dovecot mail server,,,', 'user_id': '116', 'group_id': '108', 'home_directory': '/usr/lib/dovecot', 'username': 'dovecot'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': 'Dovecot login user,,,', 'user_id': '117', 'group_id': '109', 'home_directory': '/nonexistent', 'username': 'dovenull'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '118', 'group_id': '110', 'home_directory': '/var/lib/postgrey', 'username': 'postgrey'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '119', 'group_id': '111', 'home_directory': '/var/run/opendkim', 'username': 'opendkim'},
{'passwrd': 'x', 'shell': '/bin/false', 'full_name': '', 'user_id': '120', 'group_id': '112', 'home_directory': '/home/policyd-spf', 'username': 'policyd-spf'},]

#with open('test.txt', 'a', encoding='utf-8') as f:
#    f.write('Hello world!!!\n') 
with open('test.txt', 'r', encoding='utf-8') as f: 
    num_line = 0
    for line in f:
        print("{} {}!!!".format(num_line, line.replace('\n','')))
        num_line += 1

with open('/home/maddeer/referat.txt', 'r') as referat:
    words=0
    for line in referat: 
        words += len(line.split())
    print('{} words in file'.format(words))

with open('passwd', 'r', encoding='utf-8') as f:
    fields = ['username', 'passwrd', 'group_id', 'user_id', 'full_name', 'home_directory', 'shell']
    csvdata = csv.DictReader(f, fields, delimiter=':')
    id=0
    for row in csvdata:
        id+=float(row['user_id'])
        print(row)
print(id)
with open('passwd.csv', 'w', encoding='utf-8') as f:
    fields = ['username', 'passwrd', 'group_id', 'user_id', 'full_name', 'home_directory', 'shell']
    csvdata = csv.DictWriter(f, fields, delimiter=';')
    for user in usertab:
        if user['shell'] != '/bin/false' and user['shell'] != '/usr/sbin/nologin':
            csvdata.writerow(user)

answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
with open('answers.csv', 'w', encoding='utf-8') as f:
    fields = [ 'question', 'answer' ]
    csvdata = csv.DictWriter(f, fields, delimiter=';')
    for question in answers: 
        row={fields[0]: question, fields[1]: answers[question]}
        csvdata.writerow(row)
