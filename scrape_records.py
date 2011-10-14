# scrape records from http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp
# mike tahani   m.tahani at gmail
import urllib

def scrape(dir):
    """ get all HTML pages from the site """

    base = 'http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp?start='
    end = 8120
    i = 1   # iteration

    while i < end:
        req = str(i)
        urllib.urlretrieve(base + req, filename=doc_dir+req+'.html')
        print "got", base + req
        i += 20
    return

if __name__ == '__main__':
    scrape('docs/')