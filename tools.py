from random import choice

file = open('source/tdk.txt', 'r', encoding='utf-8')
webname = open('source/webname.txt', 'r', encoding='utf-8')
place = open('source/place.txt', 'r', encoding='utf-8')
fan = open('source/fan.txt', 'r', encoding='utf-8')
domain = open('source/domain.txt', 'r', encoding='utf-8')
tdk = open('source/tdk.txt', 'r', encoding='utf-8')
file_array = []
webname_array = []
place_array = []
fan_array = []
tdk_array = []
for line in file:
    file_array.append(line.strip())
for line in webname:
    webname_array.append(line.strip())
for line in place:
    place_array.append(line.strip())
for line in fan:
    fan_array.append(line.strip())
for line in tdk:
    tdk_array.append(line.strip())

# start
for line in domain:
    for item_fan in fan_array:
        item_domain = '%s.%s' % (item_fan, line.strip())
        item_webname = choice(webname_array)
        result = item_domain + '----' + item_webname + '----' + choice(tdk_array)
        result_temp = str(result).replace('【网站标题】', item_webname)
        result_temp1 = result_temp.replace('【地名】', choice(place_array))
        result_temp2 = result_temp1.replace('【网站域名】', item_domain)
        result_temp3 = result_temp2.replace('----------', '----')
        print(result_temp3)



