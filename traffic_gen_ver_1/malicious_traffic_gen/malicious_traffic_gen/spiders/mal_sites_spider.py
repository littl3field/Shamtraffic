import scrapy
from .. import items
from global_variables import globalVariables

class MalSiteSpider(scrapy.Spider):
    name = "collectmalsites" #The name you'll use to call the spider
    start_urls = globalVariables.MAL_SITES_SOURCE
    file_of_sites = open(globalVariables.WRITE_TO_MAL_SITE_FILE,'w')

    def parse(self, response):
        items.sites = response.xpath('//strong[contains(.,"http")]/text()').extract()  #Extract the link


        for site in items.sites:                                                     #Write all the sites to the file
            self.file_of_sites.write("%s\n" % site)
