# parse records from the local copies of pages from http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp
# mike tahani   m.tahani at gmail
from BeautifulSoup import *
import csv, os

def gen_readfiles(dir):
    writer = csv.writer( open('lobbyists_new1.csv', 'wb'), dialect='excel' )
    writer.writerow( ['year','name','address','address2',
                      'employer','employer_address',
                      'employer_address2'] )
    for soup in read_files_as_soup(dir):
        table = soup.findAll( 'tr' , attrs={ 'bgcolor' : '#FFFFFF' } )
        records = ( record.contents for record in table )
        for record in records:
            fields = [ get_innertext(node) for node in record if node != '\n' ]
            writer.writerow(fields)
        print "... done"
    return

def read_files_as_soup(dir):
    """ read files from a dir, process them as BS objects """
    for filename in os.listdir(dir):
        print "processing", filename,
        yield BeautifulSoup( open( dir + filename ).read() )
        
def get_innertext(node):
    """ get the inner text of a BS node, get rid of spaces """
    innertext = ''.join(node.findAll(text=True))
    return re.sub('&nbsp;?', '', innertext)

if __name__ == '__main__':
    
    gen_readfiles('docs/')