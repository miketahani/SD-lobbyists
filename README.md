# SD Lobbyists

Last month, someone asked the NICAR mailing list about scraping a list of lobbyists from [a government website in South Dakota](http://apps.sd.gov/applications/ST12ODRS/LobbyistViewlist.asp):

> "Can anyone offer pointers or a good tutorial on building a web scraper for someone who has never done this before? I want to rustle all the fields from here -- http://bit.ly/pBE5Ph - into one file without having to copy/paste my way through 400 pages."

I wrote a scraper to collect the data, and recently updated it to reflect best-practices. Hopefully, journalists and other data nerds will find this useful.

## Dependencies

Requires BeautifulSoup (`easy_install BeautifulSoup` on Windows).

## Files

*docs/* contains the scraped pages as of Sept 2011.

### New Version

*scrape_records.py* will scan the site, collecting all records. It's pretty ugly since it's just a copy/paste from *old.py*. *parse_records.py* is the parser.

Output is in *lobbyists_new.csv*. <del>Optionally, you can return a JSON-formatted string of the data from the script, piping it to a .json file. See *parse_records.py* for usage information.</del> *dropped*

### Old Version
*old.py* is the initial version of the code. Despite using some bad practices (parsing HTML with regex), it's _a lot_ faster than the new parser, *parse_records.py*. This is owing to BeautifulSoup's overhead. *old.py* contains code to both scrape and parse the data, whereas the new version splits the tasks into separate scripts.

The output for *old.py* is in *lobbyists_old.csv*.

## Author Info
Mike Tahani, m.tahani at gmail