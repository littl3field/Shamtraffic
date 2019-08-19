import os

class globalVariables:
    '''
    Control the delay times (the higher the number, the lower the number of requests per hour)
    '''
    PEAK_TIME_DELAY = 2
    OFF_PEAK_DELAY = 5
    QUIET_TIME_DELAY = 30
    '''
    Set the timeout in seconds
    '''
    WEB_REQ_TIMEOUT = 5
    FILE_DOWNLOAD_TIMEOUT = 10

    '''
    Set the limits of how many links the spider will download starting from a particular site
    '''
    MINIMUM_LINKS_TO_FOLLOW = 5
    MAXIMUM_LINKS_TO_FOLLOW = 25

    '''
    Control the files that are used to read the top sites and the one written to
    '''
    THOUSAND_TOP_SITES_FILE = os.path.normpath(os.path.join(os.path.dirname(__file__),os.path.pardir,"file_of_sites.txt"))
    WRITE_TO_TOP_THOUSAND_SITE_FILE = os.path.normpath(os.path.join(os.path.dirname(__file__), os.path.pardir, "file_of_sites.txt"))#If you want to have a backup file with static top sites, change which one is written to so it's not overwritten

    '''
    Edit this to change the source used to gather the top sites
    '''
    TOP_SITES_SOURCE =['http://stuffgate.com/stuff/website/top-1000-sites']
