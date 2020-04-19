
import decimal


print(f'体温管理システム')
print(f'名前を入力してください。')
name = input()
print(f'現在の体温を入力してください。')
bd_temperature = decimal.Decimal(input())

def result():
    if bd_temperature <= 37.5:
        return f'{name}さんは異常ありません。'
    elif bd_temperature >37.6:
        return f'{name}さんは出社してはいけません。'


print(f'{name}さんの体温測定結果')
print(f'{name}さんの体温は{bd_temperature}です。')
print(result())
