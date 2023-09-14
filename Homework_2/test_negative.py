'''
Создать отдельный файл для негативных тестов. Функцию
проверки вынести в отдельную библиотеку. Повредить архив
(например, отредактировав его в текстовом редакторе).
Написать негативные тесты работы архиватора с командами
распаковки (e) и проверки (t) поврежденного архива
'''
from task01 import checkout_negative

folderin = "/home/nata/tst"
folderout = "/home/nata/out"
folderext = "/home/nata/folder1"
folderbad = "/home/nata/folder2"


def test_step1():
    # test1
    assert checkout_negative(f"cd {folderbad}; 7z e  arx2.7z -o{folderext} -y", "ERRORS"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout_negative(f"cd {folderbad}; 7z t arx2.7z", "ERRORS"), "test2 FAIL"


