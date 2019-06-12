import re

pattern = r'gr.y'

if re.match(pattern, "greyyyy"):
    print('match1')
if re.match(pattern, 'grayy'):
    print('match2')

pattern1 = r'^gr.y$'

if re.match(pattern1, "grey"):
    print('match3')

pattern3 = r'[aucf]'

if re.match(pattern3, "ale"):
    print('match4')

pattern4 = r'[A-Z][a-z][0-9]'

if re.search(pattern4, 'Ca6'):
    print('match5')

pattern5 = r'[^A-Z]'

if re.search(pattern5, 'dgdfgadegd545454'):
    print('match6')

pattern6 = r'egg(spam)*'

if re.match(pattern6, 'egg'):
    print('match7')
if re.match(pattern6, 'eggspamspamspam'):
    print('match8')

pattern7 = r'g+'

if re.match(pattern7, 'gggggggg'):
    print('match9')

pattern8 = r'a(bc)(de)(f(g)h)i'
m = re.match(pattern8, "abcdefghifsdgfsg")
print(m.group())
print(m.group(0))
print(m.group(2))
print(m.groups())

pattern9 = r'gr(e|a)y'

if re.match(pattern9, "gray"):
    print('match10')

pattern10 = r'(.+)\1'

if re.match(pattern10, 'wordword'):
    print('match11')