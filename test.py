import csv

# 讀取原始資料並儲存到字典中
with open('original.csv', 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.DictReader(f)
    print(f"Original file fieldnames: {reader.fieldnames}")

# 讀取比對資料並進行比對
with open('input.csv', 'r', encoding='big5', errors='replace') as f:
    reader = csv.DictReader(f)
    print(f"Input file fieldnames: {reader.fieldnames}")
