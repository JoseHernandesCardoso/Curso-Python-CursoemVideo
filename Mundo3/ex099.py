from time import sleep

def maior(*nums):
    print('-=-'*20)
    print('Analisando os valores passados...')
    sleep(0.8)
    if nums != ():
        for num in nums:
            print(num, end=' ')
            sleep(0.3)
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {max(nums) if nums != () else "0"}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
