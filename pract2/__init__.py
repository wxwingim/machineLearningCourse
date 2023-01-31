import re


# 3
pattern1 = '^\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3}$'

test1 = ['192.168.0.1', '127.0.0.1', '0.0.0.0', '0.100.200.300',
         '192.168.0.', 'a.b.c.d', '1234.2345.3456.4567']

print('3')
for i in range(len(test1)):
    result = re.match('^\d{1,3}\.{1}\d{1,3}\.{1}\d{1,3}\.{1}\d{1,3}$', test1[i])
    print(result)

# 4
print('4')
test2 = ['some text 5678.23 some text, some text 0 some text, some text 0.15 some text',
         'some text123some text, text 13,4 text, text -3.4 text']
for i in range(len(test2)):
    result = re.findall('(\s\d{1,}\.\d{1,})|(\s\d{1,}\s)', test2[i])
    print(result)

print('7')
# 7
test3 = ['<a href="/a/index.php" target="_blank"><img alt="title" src="http://test/image.png"></a>']

for i in range(len(test3)):
    result = re.findall(r'(<img/?[^\>]+>)', test3[i])
    print(result)
