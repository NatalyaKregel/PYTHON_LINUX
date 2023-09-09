'''
Задание 2
Переписать тест на Python c использованием модуля subprocess.
'''

import subprocess
'''
#!/bin/bash
result=$(cat /etc/os-release)
if [[ $result == *"22.04.3"* && $result == *"jammy"* && $? == 0 ]];
then echo "SUCCESS"
else echo "FAIL"
fi
'''
def script_1():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if ("jammy" in result.stdout and "22.04.3" in result.stdout and result.returncode == 0):
        print("SUCCESS")
    else:
        print("FAIL")

script_1()