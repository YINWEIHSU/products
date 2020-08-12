import os

#找檔案
products = []
if os.path.isfile('products.csv'):
	print('yes')
	#讀取檔案

	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',') #遇到逗點就切
			products.append([name, price])
	print(products)
else:
	print('no')



#使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price])
print(products)

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')