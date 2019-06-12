import re

pattern = r'gr.y'

if re.match(pattern, "greyyyy"):
    print('match1')
if re.match(pattern, 'grayy'):
    print('match2')

pattern1 = r'^gr.y$'

if re.match(pattern1, "grey"):
    print('match3')