from bs4 import BeautifulSoup
import re
from urllib import request
import datetime
import csv
from time import sleep

# Request URL and return response as BeautifulSoup object
def makeBeautifulSoupObject(url):            
    try:
        #print("Accessing ,", url)
        requestConn = request.urlopen(url)
        if (requestConn.getcode() != 200):
            print("Error accessing page: ", url)
        responseHTML = requestConn.read()
        requestConn.close()
        soup = BeautifulSoup(responseHTML, "lxml")
        soup.decode(eventual_encoding="unicode")
        return soup
    except:        
        print("Error accessing page and will try again in 5 seconds ,", url)
        sleep(5)
        soup = makeBeautifulSoupObject(url)
        return soup

    
def parseHTML(table_):
    record = {}
    table = BeautifulSoup(str(table_[0]), 'html.parser')

    for tr in table.find_all("tr")[1:]:
        tds = tr.find_all("td")
        # encoding the 'value' string to utf-8 and removing any non-breaking space (HTML Character)
        tmp_str = tds[1].string  # .string.encode('utf-8').replace("&nbsp;", "")
        value = str(tmp_str)  # this is the value- In Column #2 of the HTML table
        key = tds[0].string  # this is the key- In Column #1 of the HTML table        
        if key == "Date:":
            dat = str(value).replace(',', '')
            date = datetime.datetime.strptime(dat, '%B %d %Y')
            record["date"] = date
        elif key == "Time:":
            if not value == '?':
                time = re.sub("[^0-9]", "", value)
                record["time"] = time[0:2] + ":" + time[2:4]
            else:
                record["time"] = ''
        elif key == "Location:":
            if not value == '?':
                record["loc"] = str(value).replace('\n',' ')
            else:
                record["loc"] = ''
        elif key == "Operator:":
            if not value == '?':
                record["op"] = str(value).replace('\n',' ') #encode("utf-8")
            else:
                record["op"] = ''
        elif key == "Flight #:":
            if not value == '?':
                record["flight"] = str(value).replace('\n',' ')
            else:
                record["flight"] = ''
        elif key == "Route:":
            if not value == '?':
                record["route"] = str(value).replace('\n','')
            else:
                record["route"] = ''
        elif key == "Registration:":
            if not value == '?':
                record["reg"] = str(value).replace('\n',' ') #encode("utf-8")
            else:
                record["reg"] = ''
        elif key == "cn / ln:":
            if not value == '?':
                record["cnln"] = str(value).replace('\n','')
            else:
                record["cnln"] = ''
        elif key == "Aboard:":
            if not value == '?':
                s = ' '.join(value.split())
                aboard_ = s.replace('(', '').replace(')', '').split(' ')
                if aboard_[0] != '?':
                    record["aboard_total"] = aboard_[0]
                else:
                    record["aboard_total"] = 'NULL'

                passengers = aboard_[1].replace("passengers:", "")
                if passengers != '?':
                    record["aboard_passengers"] = passengers
                else:
                    record["aboard_passengers"] = 'NULL'

                crew = aboard_[2].replace("crew:", "")
                if crew != '?':
                    record["aboard_crew"] = crew
                else:
                    record["aboard_crew"] = 'NULL'
            else:
                record["aboard_total"] = 'NULL'
                record["aboard_passengers"] = 'NULL'
                record["aboard_crew"] = 'NULL'
        elif key == "Fatalities:":
            if not value == '?':
                s = ' '.join(value.split())
                fatalities_ = s.replace('(', '').replace(')', '').split(' ')

                if fatalities_[0] != '?':
                    record["fatalities_total"] = fatalities_[0]
                else:
                    record["fatalities_total"] = 'NULL'

                passengers = fatalities_[1].replace("passengers:", "")
                if passengers != '?':
                    record["fatalities_passengers"] = passengers
                else:
                    record["fatalities_passengers"] = 'NULL'

                crew = fatalities_[2].replace("crew:", "")
                if crew != '?':
                    record["fatalities_crew"] = crew
                else:
                    record["fatalities_crew"] = 'NULL'
            else:
                record["aboard_total"] = 'NULL'
                record["aboard_passengers"] = 'NULL'
                record["aboard_crew"] = 'NULL'
        elif key == "Ground:":
            if not value == '?':
                record["ground"] = str(value)
            else:
                record["ground"] = 'NULL'
        elif key == "Summary:":
            if not value == '?':
                record["summary"] = str(value).replace('\n',' ')
            else:
                record["summary"] = ''
        elif key == "AC Type:":
            if not value == '?':
                record["actype"] = str(value).replace('\n',' ')
            else:
                record["actype"] = ''
        else:
            st1 = ''.join(tds[0].string.split()).lower()
            st1 = st1.replace(':', '').replace('\n',' ')
            if not value == '?':
                record[st1] = str(value).replace('\n',' ')
            else:
                record[st1] = "NULL"
    return record

### Main Program ###

# Root URL
rooturl = "http://www.planecrashinfo.com"
# From which year data is taken
start_year = 2019 # Year 1920 contains all crash info from 1908
# to which year data is taken
end_year = 2023

# Create a new file
f = csv.writer(open("Airplane_Crashes_and_Fatalities_Since_1908_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".csv", "w", newline=''), delimiter=',')
# Header info
f.writerow(["Date", "Time", "Location", "Operator", "Flight #", "Route", "AC Type", "Registration", "cn/ln", "Aboard","Aboard Passangers","Aboard Crew", "Fatalities", "Fatalities Passangers","Fatalities Crew", "Ground", "Summary"])

for i in range(start_year, end_year + 1, 1):
    # sleep to overcome Server connection refused error
    sleep(0.1)
    year_start = datetime.datetime.utcnow()
    # appending the path (year) to the url hostname
    # Sample page : http://www.planecrashinfo.com/2008/2008.htm
    newurl = rooturl + "/" + str(i) + "/" + str(i) + ".htm"
    #Get the main page for each year    
    soup = makeBeautifulSoupObject(newurl)
    tables = soup.find_all('table')

    #Each page contains the sumamry crash info
    for table in tables:
        # finding the no. of records for the given year
        number_of_rows = len(table.findAll(lambda tag: tag.name == 'tr' and tag.findParent('table') == table))        
        print("Year: ",i, " | ", number_of_rows-1)
        for j in range(1, number_of_rows, 1):
            # appending the row number to sub-path of the url, and building the final url that will be used for sending http request
            #Sample : http://www.planecrashinfo.com/2008/2008-1.htm
            accident_url = newurl.replace(".htm", "") + "-" + str(j) + ".htm"
            web_record = makeBeautifulSoupObject(accident_url)
            # removing all the boilerplate html code except the data table
            table_details = web_record.find_all('table')
            #Parse table and return crash record
            crashRecord = parseHTML(table_details)
            #Write crash record to file            
            f.writerow([crashRecord["date"].strftime('%m/%d/%Y'),
                        crashRecord["time"],
                        crashRecord["loc"],
                        crashRecord["op"],
                        crashRecord["flight"],
                        crashRecord["route"],
                        crashRecord["actype"],
                        crashRecord["reg"],
                        crashRecord["cnln"],
                        crashRecord["aboard_total"],
                        crashRecord["aboard_passengers"],
                        crashRecord["aboard_crew"],
                        crashRecord["fatalities_total"],
                        crashRecord["fatalities_passengers"],
                        crashRecord["fatalities_crew"],
                        crashRecord["ground"],
                        crashRecord["summary"]
                        ])