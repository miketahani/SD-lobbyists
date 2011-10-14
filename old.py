# grab south dakota lobbyist info - the ugly/hacky version
# mike tahani   m.tahani at gmail

import urllib, re, os, csv

def getdocs(doc_dir):
    """ get the raw documents from the gov site """

    base = 'http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp?start='
    end = 8120
    i = 1   # iteration

    while i < end:
        req = str(i)
        urllib.urlretrieve(base + req, filename=doc_dir+req+'.html')
        print "got", base + req
        i += 20
    return
    
def getfields(writer, data):
    """ get all fields from a document's raw data (& write to csv) """
    
    chunks = re.compile('\<tr bgcolor=\"#FFFFFF\"\>(.+?)\</tr\>', re.DOTALL)    
    res = chunks.findall(data)
    
    for chunk in res:
        fields = chunk.split('<td>')
        row = filter(None, [ re.sub('\<.+?\>|\&nbsp;','',field).strip() for field in fields ])
        writer.writerow(row)
    return

def main():    
    doc_dir = 'docs/'
    #get_docs(doc_dir)  # run once

    hdrs = ['year','name','address','address2','employer','employer_address',
            'employer_address2']
    writer = csv.writer(open('lobbyists_old.csv', 'wb'), dialect='excel')
    writer.writerow(hdrs)
    
    for f in os.listdir(doc_dir):
        data = open(doc_dir + f).read()
        getfields(writer, data)
    return

if __name__ == '__main__':
    main()