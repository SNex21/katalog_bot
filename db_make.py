from crud import create_device, s

for i in range(80):
    title, params = input().split('_')
    price = input().replace(' руб.', '')
    company = 'Apple'
    device_type = 'Телефон'
    decr = None
    dev = {'device_title': title, 'description': decr, 'company':company, 'params':params,  'device_type':device_type, 'price': price}
    create_device(s, dev)