import scrapy
from .. import items
from global_variables import globalVariables

class TopSiteSpider(scrapy.Spider):
    name = "collecttopsites" #The name you'll use to call the spider
    start_urls = globalVariables.TOP_SITES_SOURCE

    def parse(self, response):
        items.sites = response.xpath('//a[contains(@href,"http")]/@href').extract()  #Extract the link
        file_of_sites = open(globalVariables.WRITE_TO_TOP_THOUSAND_SITE_FILE,'w')

        for site in items.sites:                                                     #Write all the sites to the file
            file_of_sites.write("%s\n" % site)
