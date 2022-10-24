import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(s)
        sys.stdout.flush()

        time.sleep(random.random() * 0.3)

mengetik('Jangan Lupa Subscribe Channel User Eror21 \nselamat menonton\nTerimakasih.')
