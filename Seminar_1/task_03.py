'''
Задание 3
Делимся на команды для выполнения следующей задачи:
Доработать тест из предыдущего задания таким образом,
чтобы вывод сохранялся построчно в список и в тесте проверялось,
что в этом списке есть строки VERSION="22.04.1 LTS (Jammy
Jellyfish)" и VERSION_CODENAME=jammy . Проверка должна
выполняться только если код возврата равен 0.
'''
import subprocess
def script_1():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    #print(result.stdout)
    if result.returncode == 0:
        res = result.stdout.split("\n")
        print(res)
        if "VERSION_CODENAME=jammy" in res and 'VERSION="22.04.3 LTS (Jammy Jellyfish)"' in res:
            print("SUCCESS")
        else:
            print("FAIL")

script_1()
