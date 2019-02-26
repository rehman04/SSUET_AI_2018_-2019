#are text matching patterns
import re
#search
#print(re.search('hello', 'hello world'))
'''patterns = ['term1', 'term2']
text = 'this is a text with term1,but not the other term'
for pattern in patterns:
    print('searching for "%s" in : \n "%s"' % (pattern, text))
if re.search(pattern, text):
    print('\n Match was found.\n')
else:
    print('no match was found \n')

#print(re.search('h', 'w'))

match = re.search(patterns[0], text)
print(match.start())
print(match.end())'''

#split
'''split_term='@'
phrase='what is ur email, is it hello@gmail.com?'
print(re.split(split_term,phrase))'''

#findall
'''print(re.findall('match','there is a match, there is another match tonight'))

def Multi_re_find(patterns,phrase):
    print(phrase)
    print()
    for patternss in patterns:
        print('search the phrase using the re check: %r' %patternss)
        print(re.findall(patternss,phrase))
        print('\n')
print()
test_phrase='sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns=['sd*',
               'sd+',
               'sd?',
               'sd{4}',
               'sd{3,4}',
               ]
Multi_re_find(test_patterns,test_phrase)'''

#character set
'''def Multi_re_find(patterns,phrase):
    print(phrase)
    print()
    for patternss in patterns:
        print('search the phrase using the re check: %r' %patternss)
        print(re.findall(patternss,phrase))
        print('\n')
print()
test_phrase='sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns=['[sd]',
               'd[sd]{2}']
Multi_re_find(test_patterns,test_phrase)'''

#exclusion
'''test_phrase='this is a string! but it has punctuation. how can we remove it?'
print(re.findall('[^!.?]+',test_phrase))'''

#character ranges
'''test_phrase='this is an example sentence. Lets see if we can find some letters.'
def Multi_re_find(patterns,phrase):
    print(phrase)
    print()
    for patternss in patterns:
        print('search the phrase using the re check: %r' %patternss)
        print(re.findall(patternss,phrase))
        print('\n')
print()
test_patterns=['[a-z]+',
               '[A-Z]+',
               '[a-zA-Z]+',
               '[A-Z][a-z]+']
Multi_re_find(test_patterns,test_phrase)'''

#escape code
def Multi_re_find(patterns,phrase):
    print(phrase)
    print()
    for patternss in patterns:
        print('search the phrase using the re check: %r' %patternss)
        print(re.findall(patternss,phrase))
        print('\n')
print()
test_phrase='This is a string with some numbers 12345 and a symbol #hastag'
test_patterns=[r'\d+',
               r'\D+',
               r'\s+',
               r'\S+',
               r'\w+',
               r'\W+']
Multi_re_find(test_patterns,test_phrase)