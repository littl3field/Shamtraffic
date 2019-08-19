import os

class globalVariables:
    '''
    Control the delay times (the higher the number, the lower the number of requests per hour)
    '''
    PEAK_TIME_DELAY = 40
    OFF_PEAK_DELAY = 60
    QUIET_TIME_DELAY = 100

    '''
    Set the timeout in seconds
    '''
    WEB_REQ_TIMEOUT = 5
    FILE_DOWNLOAD_TIMEOUT = 60

    '''
    Set the limits of how many links the spider will download starting from a particular site
    '''
    MINIMUM_LINKS_TO_FOLLOW = 5
    MAXIMUM_LINKS_TO_FOLLOW = 25

    '''
    Control the files that are used to read the top sites and the one written to
    '''
    MAL_SITES_FILE = os.path.normpath(os.path.join(__file__, os.path.pardir, os.path.pardir,"file_of_sites.txt"))
    WRITE_TO_MAL_SITE_FILE = os.path.normpath(os.path.join(__file__, os.path.pardir, os.path.pardir,"file_of_sites.txt")) #If you want to have a backup file with static mal sites, change which one is written to so it's not overwritten

    '''
    Edit this to change the source used to gather the top sites
    '''
    MAL_SITES_SOURCE =['https://quttera.com/lists/malicious',
    'https://quttera.com/lists/malicious?page=1',
    'https://quttera.com/lists/malicious?page=2',
    'https://quttera.com/lists/malicious?page=3',
    'https://quttera.com/lists/malicious?page=4'
    'https://quttera.com/lists/malicious?page=5'

    ]
