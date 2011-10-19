# parse records from the local copies of pages from http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp
# mike tahani   m.tahani at gmail
from BeautifulSoup import *
import csv, os

def html_to_csv(dir):
    """ open directory of local SD-lobbyists pages and convert them to csv """
    writer = csv.writer( open('lobbyists_new.csv', 'wb'), dialect='excel' )
    writer.writerow( ['year','name','address','address2',
                      'employer','employer_address',
                      'employer_address2'] )    # headers
    for soup in read_files_as_soup(dir):
        # find all tr tags with a certain attribute:
        table = soup.findAll( 'tr' , attrs={ 'bgcolor' : '#FFFFFF' } )
        # generator expression to get contents of all tr tags:
        records = ( record.contents for record in table )
        for record in records:
            # get table fields from the records:
            fields = [ get_innertext(node) for node in record if node != '\n' ]
            writer.writerow(fields) # write the record's fields as a csv row
        print "... done"
    return

def read_files_as_soup(dir):
    """ read files from a dir, process them as BS objects """
    for filename in os.listdir(dir):
        print "processing", filename,
        # convert local HTML page to a BS object:
        yield BeautifulSoup( open( dir + filename ).read() )
        
def get_innertext(node):
    """ get the inner text of a BS node, get rid of spaces """
    innertext = ''.join(node.findAll(text=True))    # get text only, no tags
    return re.sub('&nbsp;?', '', innertext) # get rid of some HTML spaces

if __name__ == '__main__':
    
    html_to_csv('docs/')