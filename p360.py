file = open('/Users/hang/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/ccdb0e66a66a3d84cf62970d4d983ef3/Message/MessageTemp/03da3995822e8dba1124d139b6e0106b/File/1152885')
s = '~'
list = []
while s != 'end':
    data = {}
    s = file.readline()
    data['barcode'] = s
    while s != '\n' and s != 'end':
        s = file.readline()
        if 'howOldUser' in s and 'Dubbo Request Start' in s or '[MOP_TRACE][getMopRequest]' in s:
            data['MCOM-1'] = s
        if 'Mop Http Request' in s:
            data['MCOM-2'] = s
        if 'call p360' in s:
            data['P360-1'] = s
        if 'receive str' in s:
            data['P360-2'] = s
    print data
    list.append(data)

for item in list:
    print item['barcode'][0:len(item['barcode'])-1]+'@',
print
for item in list:
    print item['MCOM-1'][0:23]+'@',
print
for item in list:
    print item['MCOM-1'][0:len(item['MCOM-1'])-1]+'@',
print
for item in list:
    print item['MCOM-2'][0:23]+'@',
print
for item in list:
    print item['MCOM-2'][0:len(item['MCOM-2'])-1]+'@',
print
for item in list:
    print item['barcode'][0:len(item['barcode'])-1]+'@',
print
for item in list:
    print item['P360-1'][0:23]+'@',
print
for item in list:
    print item['P360-1'][0:len(item['P360-1'])-1]+'@',
print
for item in list:
    print item['P360-2'][0:23]+'@',
print
for item in list:
    print item['P360-2'][0:len(item['P360-2'])-1]+'@',
print

