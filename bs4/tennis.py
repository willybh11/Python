import urllib2
import bs4 as bs

sauce = urllib2.urlopen('https://www.germantownfriends.org/athletics/teams/team-details/~athletics-team-id/276').read()
soup = bs.BeautifulSoup(sauce, 'html.parser')

raw = soup.find('div', attrs={'class':'fsListItems'})
text = str(raw.text)
text = text.replace('\t','').replace('\n\n','\n').replace('\n\n','\n').replace('Subscribe to Alerts','').replace('GFS Tennis Courts','').replace('\nvs. \n','  vs.  ')
text = text.replace('\nAway\n','Away: ').replace('\nHome\n','Home')
textlist = text.split('\n')
for i in range(len(textlist)):
    line = textlist[i]
    if 'AM' in line or 'PM' in line:
        if len(line[:line.index(":")].replace(' ','')) == 2:
            line = ' '+line
        textlist[i] = line


newtext = '\n'.join(textlist)
newtext = newtext.replace('\n ',' - ')
print newtext
