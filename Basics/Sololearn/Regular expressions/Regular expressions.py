import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print('Match')
else:
    print('No match')

if re.search(pattern, 'eggspamspams'):
    print('Search result found')
    print(re.search(pattern, 'eggspamspams').group())
    print(re.search(pattern, 'eggspamspams').start())
    print(re.search(pattern, 'eggspamspams').end())
    print(re.search(pattern, 'eggspamspams').span())
else:
    print('No search result found')

print(re.findall(pattern, 'eggspamsausagespamsdd'))