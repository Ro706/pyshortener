import pyshorteners
from termcolor import colored
from pyfiglet import Figlet

f=Figlet(font='slant')
print (f.renderText('PyShortenerS'))
print (colored('    --made by Ro706','magenta'))
def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

if __name__=="__main__":
    url = input(colored("Enter link to shorten: ",'blue'))
    print(colored(f"\n{shorten( url)}",'green'))
