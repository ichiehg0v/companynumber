import csv

# 讀取原始資料並儲存到字典中
original_data = {}
with open('original.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        original_data[row['#id']] = row['name']

# 讀取比對資料並進行比對
with open('input.csv', 'r', encoding='big5') as f:
    reader = csv.DictReader(f)
    input_data = [row for row in reader]

# 進行比對並儲存結果
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = input_data[0].keys()
    fieldnames = list(fieldnames)
    fieldnames.append('核對結果')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for row in input_data:
        if row['#id'] in original_data:
            if row['name'] == original_data[row['#id']]:
                row['核對結果'] = 'ok'
            else:
                row['核對結果'] = original_data[row['#id']]
        else:
            row['核對結果'] = '統編不存在'
        writer.writerow(row)
