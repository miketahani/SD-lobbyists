require 'open-uri'

def scrape(dir)
  # fetch pages from SD-lobbyists site

  base  = "http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp?start="
  total = 8120  # total number of records
  i     = 1 # iteration
  step  = 20  # number of records per page

  while i < total
    rec = i.to_s
    puts 'getting ' + base + rec 
    page = open(base + rec).read
    out = open(dir + rec + '.html', 'w')
    out.write(page)
    out.close
    i += step
  end
end

scrape "pages/"