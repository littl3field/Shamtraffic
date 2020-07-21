# Shamtraffic



           ███████╗██╗  ██╗ █████╗ ███╗   ███╗████████╗██████╗  █████╗ ███████╗███████╗██╗ ██████╗
           ██╔════╝██║  ██║██╔══██╗████╗ ████║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔════╝
           ███████╗███████║███████║██╔████╔██║   ██║   ██████╔╝███████║█████╗  █████╗  ██║██║     
           ╚════██║██╔══██║██╔══██║██║╚██╔╝██║   ██║   ██╔══██╗██╔══██║██╔══╝  ██╔══╝  ██║██║     
           ███████║██║  ██║██║  ██║██║ ╚═╝ ██║   ██║   ██║  ██║██║  ██║██║     ██║     ██║╚██████╗
           ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝ ╚═════╝
           is a Scrapy tool to generate malicious traffic 
           
# Info 

Prep:

```
Pip install scrapy
```

Run: 
    
scrapy crawl <spider-name>

Spiders:

##malicious_traffic_gen
collectmalsites - Compile a list of malicious sites (you don't need to run this spider everytime. 
                  Once you've got a list you'll only want to re-run it if you want to update the list.

crawlmalsites - Activate the spider. It will make requests to malicious sites and download files

##traffic_gen
collecttopsites - Compile a list of the top sites (see: collectmalsites)

crawltopsites - Active the spider. It'll make requests and download files.

Files:
Downloaded files will appear in a 'download_files' folder in the respective directories
The compiled site names will appear in the files 'file_of_sites.txt' in the respective directories
The settings for each can be found in the global_variables file in the respective directories

***WARNING***
Make sure that you're running the malicious spider in a virtual machine or the sandbox. 
It will start making automatic requests to malicious domains.
                                                                                       
