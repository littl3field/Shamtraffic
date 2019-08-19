
import scrapy
import random
import re
import urlparse
from global_variables import globalVariables
import datetime

class CrawlTopSitesSpider(scrapy.Spider):
    name= 'crawlmalsites'                               #This is the name that you use to refer to this spider
    file_of_sites = open(globalVariables.MAL_SITES_FILE,'r')     #The file which holds the top mal sites
    start_urls = file_of_sites.read().split('\n')       #Initialise the spider to hold the URLS
    number_visited = 0                                  #Monitor how many links the spider has followed starting at a particular site
    number_to_visit = random.randrange(globalVariables.MINIMUM_LINKS_TO_FOLLOW,globalVariables.MAXIMUM_LINKS_TO_FOLLOW)  #Determine how many links to follow
    #log_file = open("./log.txt","a")  #Use for debugging
    custom_settings = {
        'DOWNLOAD_DELAY': globalVariables.OFF_PEAK_DELAY,
        'DOWNLOAD_TIMEOUT': globalVariables.WEB_REQ_TIMEOUT
    }

    '''
    Parse each site in the list of urls - and each of the urls in the callback
    '''
    def parse(self, response):
        self.number_visited += 1 #The spider has visited one more site down this path
        download_paths = response.xpath('//a[contains(@href,".pdf") or contains(@href, ".exe") or contains(@href, ".doc") or contains(@href,".txt")]/@href').extract() ###For each PDF, exe, doc, or txt file found, add it to a list
        all_paths = response.xpath('//a[contains(@href,"http")]/@href').extract()   #Collect all links
        site_paths = [x for x in all_paths if x not in download_paths]              #Determine which links are to be followed and which are to be downloaded
        for download in download_paths:                                             #Pass all the download links to the download function
            download_url = urlparse.urljoin(response.url,download)
            yield scrapy.Request(download_url,callback = self.saveDownloads)
        if(len(all_paths) != 0 and self.number_visited < self.number_to_visit):     #IF there are any paths to visit, and the spider is still allowed to visit more
            next_url_number = random.randrange(0,len(site_paths))                   #Choose a random link to follow
            next_url = urlparse.urljoin(response.url,site_paths[next_url_number])
            yield scrapy.Request(next_url, callback = self.parse)                   #Pass the new URL to take as the root of the parse function
        else:
            self.number_visited = 0
            self.adjustTime(datetime.datetime.now().hour) #checks done after one thread is explored, otherwise it heavily impacts performance

    '''
    Control the speed of download depending on the time of day
    '''
    def adjustTime(self, time):
        if (time > 9 and time < 10):
            self.custom_settings['DOWNLOAD_DELAY'] = globalVariables.PEAK_TIME_DELAY
        elif(time > 12 and time < 13):
            self.custom_settings['DOWNLOAD_DELAY'] = globalVariables.PEAK_TIME_DELAY
        elif(time > 20 or time < 6):
            self.custom_settings['DOWNLOAD_DELAY'] = globalVariables.QUIET_TIME_DELAY
        else:
            self.custom_settings['DOWNLOAD_DELAY'] = globalVariables.OFF_TIME_DELAY

    '''
    Save the downloaded files
    '''
    def saveDownloads(self, response):
        new_url = re.search('\/{1}[^/]+\.\w+$', str(response.url)).group(0) #Extract the file name
        self.custom_settings['DOWNLOAD_TIMEOUT'] = globalVariables.FILE_DOWNLOAD_TIMEOUT
        with open("./downloaded_files/" + new_url,"wb") as f:    #Set the file path for the downloaded documents here
            pass
            ##f.write(response.body)
        self.custom_settings['DOWNLOAD_TIMEOUT'] = globalVariables.WEB_REQ_TIMEOUT
