# parse records from the local copies of pages from http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp
# mike tahani   m.tahani at gmail

from BeautifulSoup import *
import re, json, csv, os, sys

def load_file(filename):
    """ open a file and make it a BS object """
    f = open(filename).read()
    return BeautifulSoup(f)

def get_table_entries(soup):
    """ get table entries by <tr> tag """
    tags = soup.findAll( 'tr' , attrs={ 'bgcolor' : '#FFFFFF' } )   # find all tr tags with "bgcolor='#FFFFFF'"
    tag_contents = [ tag.contents for tag in tags ]                 # get tag contents (fields)
    hdrs = ['year','name','address','address2','employer','employer_address',
            'employer_address2']    # headers
    entries = []    # collection of fields
    for entry in tag_contents:
        # get the inner text of the BS nodes found in each table entry:
        fields = [get_innertext(node) for node in entry if node != '\n']
        # add appropriate headers, append entry data to master entry collection
        entries.append( dict( zip( hdrs, fields ) ) ) 
    return entries

def get_all_entries(dir):
    """ get all entries from all local copies of tables in dir """
    all_entries = []    # collection of all fields from all table entries
    for page in os.listdir(dir):
        print "processing", page
        # collect entries from each table on each page
        all_entries += get_table_entries( load_file( dir + page ) )
    return all_entries

def get_innertext(node):
    """ get the inner text of a BS node, get rid of spaces """
    innertext = ''.join(node.findAll(text=True))
    return re.sub('&nbsp;?', '', innertext)

def output_csv(entries, filename):
    """ write csv output of entries to filename; expects a list of dicts """
    hdrs = ['year','name','address','address2','employer','employer_address',
            'employer_address2']    # headers
    # open a csv dict writer object for excel formatting:
    writer = csv.DictWriter(open(filename, 'wb'), hdrs, dialect='excel')
    # write the headers (must pass it as a dict to DictWriter):
    writer.writerow( dict( (h,h) for h in hdrs ))
    for entry in entries:
        # write all entries to the csv file
        writer.writerow(entry)
    return

def output_json(entries):
    """ print json output of entries; expects a python object """
    return json.dumps(entries)

if __name__ == '__main__':
    
    output_csv(get_all_entries('docs/'), 'lobbyists_new.csv')
    #output_json(get_all_entries('docs/')) # usage: pipe the output to a .json file