import re

pattern = re.compile(r'is')

""" Reference : https://www.youtube.com/watch?v=K8L6KVGG-7o&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=30 """

str1 = '''Mastering Python is *not* just about getting the books and courses to study—to be successful you also need a way to
stay motivated and to grow your abilities in the long run.Many Pythonistas I know are struggling with this.It's simply a lot less
fun to build your Python skills completely alone.If you're a self-taught developer with a non-technical day job it's hard to grow
your skills all by yourself.And with no coders in your personal peer group, there's nobody to encourage or support you in your
endeavor of becoming a better developer.'''

print(f'{"#"*25} finditer example. provide match with extra info {"#"*25}')
matches = pattern.finditer(str1)
for match in matches:
    print(match)

print(f'{"#"*25} findall example {"#"*25}')
matches = pattern.findall(str1)
for match in matches:
    print(match)

urls = '''
https://www.google.com
http://kas.com
https://youtune.com
https://isro.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print('#' * 150)
    print(match)
    print(match.group(0), end='\t\t')
    print(match.group(1), end='\t\t')
    print(match.group(2), end='\t\t')
    print(match.group(3))

# substitue using backreference
new_url = pattern.sub(r'\2\3', urls)
print(new_url)
