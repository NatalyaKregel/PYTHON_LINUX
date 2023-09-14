import subprocess
import zlib
from typing import Any


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


def get_crc32(cmd: Any) -> str:
    crc32_res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return crc32_res.stdout.strip()


def calc_crc32(file_path: Any) -> str:
    with open(file_path, "rb") as f:
        crc32_hash_res: int = zlib.crc32(f.read())
    return format(crc32_hash_res & 0xFFFFFFFF, '08x')




