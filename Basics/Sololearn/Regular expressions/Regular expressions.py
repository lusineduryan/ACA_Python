import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print('Match')
else:
    print('No match')

if re.search(pattern, 'eggspamspams'):
    print('Search result found')
else:
    print('No search result found')

print(re.findall(pattern, 'eggspamsausagespamsdd'))