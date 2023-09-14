from task01 import checkout
from task01 import calc_crc32

path_dir = '/home/nata/tst'
path_arx = '/home/nata/arx2'


def test_step1():
    # test1
    assert checkout(f"cd {path_dir}; 7z a {path_arx}", "Everything is Ok"), "Test1 FAIL"


def test_step2():
    # test2
    assert checkout(f"cd {path_dir}; 7z u {path_arx}", "Everything is Ok"), "Test2 FAIL"


def test_step3():
    # test3
    assert checkout(f"cd {path_dir}; 7z d {path_arx}", "Everything is Ok"), "Test3 FAIL"


def test_step4():
    # test4
    assert checkout(f"cd {path_dir}; 7z l {path_arx}", "Everything is OK"), "Test4 Fail"


def test_step5():
    # test5
    assert checkout(f"cd {path_dir}; 7z x arx1.7z -o{path_arx}", "Everything is OK"), "Test5 Fail"


def test_step6(data=None):
    # test6
    assert calc_crc32(data, 'hash_crc') == checkout(f'7z h {path_arx}', "Everything is OK"), "Test6 FAIL"

