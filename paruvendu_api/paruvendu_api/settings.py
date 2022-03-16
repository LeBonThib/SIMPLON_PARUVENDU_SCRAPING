# Scrapy settings for paruvendu_api project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'paruvendu_api'

SPIDER_MODULES = ['paruvendu_api.spiders']
NEWSPIDER_MODULE = 'paruvendu_api.spiders'

# When doing broad crawls you are often only interested in the crawl rates you get and any errors found. These stats are reported by Scrapy when using the INFO log level. In order to save CPU (and log storage requirements) you should not use DEBUG log level when preforming large broad crawls in production.
LOG_LEVEL = 'DEBUG'
LOG_ENABLED = False

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'paruvendu_api (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 399,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# The default global concurrency limit in Scrapy is not suitable for crawling many different domains in parallel, so you will want to increase it. How much to increase it will depend on how much CPU and memory you crawler will have available.
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 10
ROTATING_PROXY_PAGE_RETRY_TIMES = 10

# Currently Scrapy does DNS resolution in a blocking way with usage of thread pool. With higher concurrency levels the crawling could be slow or even fail hitting DNS resolver timeouts. Possible solution to increase the number of threads handling DNS queries. The DNS queue will be processed faster speeding up establishing of connection and crawling overall.
REACTOR_THREADPOOL_MAXSIZE = 30

# Scrapy's default scheduler priority queue is 'scrapy.pqueues.ScrapyPriorityQueue'. It works best during single-domain crawl. It does not work well with crawling many different domains in parallel
# SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'

# Retrying failed HTTP requests can slow down the crawls substantially, specially when sites causes are very slow (or fail) to respond, thus causing a timeout error which gets retried many times, unnecessarily, preventing crawler capacity to be reused for other domains.
RETRY_ENABLED = False

# Unless you are crawling from a very slow connection (which shouldn't be the case for broad crawls) reduce the download timeout so that stuck requests are discarded quickly and free up capacity to process the next ones.
DOWNLOAD_TIMEOUT = 15

# Consider disabling redirects, unless you are interested in following them. When doing broad crawls it's common to save redirects and resolve them when revisiting the site at a later crawl. This also help to keep the number of request constant per crawl batch, otherwise redirect loops may cause the crawler to dedicate too many resources on any specific domain.
REDIRECT_ENABLED = True

# If you still want to process response codes outside that range, you can specify which response codes the spider is able to handle using the handle_httpstatus_list spider attribute or HTTPERROR_ALLOWED_CODES setting.
HTTPERROR_ALLOWED_CODES = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies unless you really need. Cookies are often not needed when doing broad crawls (search engine crawlers ignore them), and they improve performance by saving some CPU cycles and reducing the memory footprint of your Scrapy crawler.
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#  'paruvendu_api.middlewares.DigBickScrapingSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'paruvendu_api.middlewares.DigBickScrapingDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
""" ITEM_PIPELINES = {
    'paruvendu_api.pipelines.JsonWriterPipeline': 300,
} """

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

ROTATING_PROXY_LIST_PATH = './paruvendu_api/outputs/proxy_list.txt'

ROTATING_PROXY_LIST = [
'80.48.119.28:8080',
'41.186.44.106:3128',
'103.148.72.192:80',
'169.57.1.85:8123',
'107.151.182.247:80',
'134.195.101.198:80',
'202.136.165.22:80',
'5.181.171.135:8085',
'167.114.96.27:9300',
'194.5.193.183:80',
'191.96.42.80:8080',
'23.81.71.140:80',
'139.99.237.62:80',
'198.11.173.185:80',
'88.198.24.108:8080',
'20.47.108.204:8888',
'8.214.41.50:80',
'103.80.1.2:80',
'47.91.44.217:8000',
'185.88.37.126:8085',
'190.119.199.20:57333',
'154.79.242.178:1686',
'176.9.75.42:8080',
'129.226.148.192:443',
'138.201.145.164:8080',
'47.245.11.194:80',
'52.252.96.156:80',
'188.138.89.50:5566',
'202.65.158.237:84',
'41.77.13.186:53281',
'80.244.229.102:10000',
'45.5.119.242:999',
'185.82.98.4:9091',
'150.238.200.205:3128',
'52.169.143.106:8080',
'45.70.15.6:8080',
'20.105.253.176:8080',
'3.136.59.77:80',
'45.115.253.97:1337',
'35.210.27.183:80',
'129.226.127.36:80',
'121.1.41.162:111',
'185.88.37.138:8085',
'37.232.183.74:53281',
'165.16.0.89:1981',
'173.230.145.224:3128',
'116.206.243.50:80',
'110.235.250.155:8080',
'103.101.17.171:8080',
'177.53.155.22:999',
'113.160.206.37:55138',
'50.250.56.129:46456',
'79.142.95.90:55443',
'197.232.65.40:55443',
'85.25.132.9:5566',
'185.20.198.210:22800',
'62.152.75.110:50287',
'188.138.101.167:5566',
'167.71.199.228:8080',
'20.94.229.106:80',
'20.94.230.158:80',
'129.213.183.152:80',
'183.91.0.120:3128',
'47.245.12.42:80',
'195.158.18.236:3128',
'158.181.21.247:8081',
'78.157.57.182:80',
'152.228.163.151:80',
'202.150.150.211:8080',
'85.25.4.27:5566',
'192.236.160.186:80',
'185.88.37.73:8085',
'103.73.102.174:60080',
'131.72.224.202:55443',
'201.120.27.15:53281',
'46.246.80.6:8888',
'157.230.255.209:8888',
'213.230.121.116:3128',
'43.255.113.232:8082',
'121.240.20.207:80',
'213.232.123.133:8085',
'123.231.238.221:80',
'209.250.253.162:59394',
'194.233.73.109:443',
'190.100.95.229:3128',
'104.168.77.133:3128',
'158.140.169.101:10000',
'1.20.166.142:8080',
'181.188.206.40:999',
'190.171.80.91:6969',
'160.16.242.164:3128',
'171.244.140.121:8118',
'43.224.10.37:6666',
'95.66.142.11:8080',
'37.48.81.23:51327',
'103.18.77.236:8080',
'162.217.248.126:3128',
'194.163.183.183:3128',
'185.88.37.185:8085',
'185.88.37.136:8085',
'185.88.37.154:8085',
'118.70.109.148:55443',
'41.65.0.195:1981',
'103.209.248.86:8080',
'47.251.5.248:80',
'51.81.80.44:80',
'61.255.239.33:8008',
'203.202.255.67:8080',
'212.34.1.110:8080',
'109.75.145.152:15392',
'103.73.194.2:80',
'182.53.197.156:43060',
'37.61.220.235:1080',
'118.179.173.253:40836',
'134.209.216.204:3130',
'52.250.1.188:80',
'176.214.46.116:8080',
'8.210.83.33:80',
'81.252.38.12:8080',
'190.14.249.217:999',
'45.229.58.33:999',
'200.106.187.252:999',
'119.59.125.189:3128',
'191.97.18.177:999',
'68.183.65.79:3128',
'141.11.246.249:3128',
'115.124.79.92:8080',
'103.109.59.242:53281',
'86.123.166.13:8080',
'89.165.113.204:48217',
'213.97.45.73:8083',
'103.241.227.117:6666',
'202.62.67.209:53281',
'182.253.108.186:8080',
'101.255.77.243:8080',
'186.47.97.122:8080',
'211.43.214.205:80',
'177.128.115.222:999',
'154.85.35.235:8888',
'190.160.181.220:8118',
'197.254.97.248:80',
'101.53.154.137:2008',
'50.233.42.98:51696',
'103.194.175.86:8080',
'5.131.243.252:8080',
'47.88.95.28:7328',
'176.56.107.88:44887',
'173.82.149.243:8080',
'194.114.128.149:61213',
'187.217.54.84:80',
'185.61.152.137:8080',
'178.253.244.250:6666',
'168.205.100.36:8080',
'46.0.203.186:8080',
'188.138.11.39:5566',
'185.92.223.62:59394',
'79.143.87.140:9090',
'34.93.243.67:80',
'66.94.120.161:443',
'101.255.77.6:8080',
'94.73.239.124:55443',
'185.88.37.112:8085',
'212.120.186.39:60963',
'212.50.37.253:8083',
'1.179.148.9:55636',
'137.184.197.190:80',
'36.255.211.1:54623',
'185.88.37.124:8085',
'103.107.94.2:52827',
'187.216.93.20:55443',
'185.41.154.174:3128',
'149.5.38.1:8080',
'179.42.145.23:8081',
'181.30.228.13:3128',
'218.185.234.197:8080',
'18.163.194.152:80',
'47.74.152.29:8888',
'200.105.215.18:33630',
'72.47.152.224:55443',
'117.54.114.96:80',
'62.138.3.125:5566',
'103.158.121.79:8080',
'74.207.235.154:8082',
'85.25.119.241:5566',
'62.138.8.42:5566',
'114.5.199.194:8182',
'1.20.217.52:8080',
'197.254.97.253:80',
'47.243.101.11:8118',
'185.108.141.19:8080',
'190.0.17.66:8080',
'176.236.232.67:9090',
'114.5.199.196:8182',
'170.155.5.235:8080',
'179.61.229.163:999',
'36.92.43.107:8080',
'185.108.141.114:8080',
'139.5.151.178:63123',
'187.95.28.251:20183',
'185.175.119.113:47174',
'68.183.43.141:80',
'167.172.63.35:80',
'46.20.115.218:80',
'157.245.33.179:80',
'3.11.161.63:80',
'3.11.162.224:80',
'206.189.114.127:80',
'159.65.51.134:80',
'206.189.16.11:80',
'178.128.45.83:80',
'3.11.250.248:80',
'3.11.189.228:80',
'68.183.45.241:80',
'68.183.39.179:80',
'46.101.49.215:80',
'46.101.51.120:80',
'3.11.29.178:80',
'3.10.244.148:80',
'3.10.255.67:80',
'3.10.39.50:80',
'206.189.115.97:80',
'139.59.166.57:80',
'139.59.184.130:80',
'206.189.27.120:80',
'178.128.160.79:80',
'157.245.34.18:80',
'139.162.238.20:80',
'159.65.49.101:80',
'159.65.48.122:80',
'178.128.170.17:80',
'178.128.165.77:80',
'178.128.165.101:80',
'178.128.44.88:80',
'142.93.35.88:80',
'138.68.144.74:80',
'138.68.146.0:80',
'139.59.188.227:80',
'139.59.166.155:80',
'139.59.167.128:80',
'3.10.60.69:80',
'142.93.40.67:80',
'142.93.36.241:80',
'25.254.97.235:80',
'82.113.150.67:80',
'31.186.234.58:80',
'5.254.97.212:80',
'25.254.97.171:80',
'5.254.97.199:80',
'213.185.116.152:80',
'109.74.197.124:80',
'109.204.121.123:80',
'31.222.165.14:80',
'78.141.203.40:80',
'178.62.72.23:80',
'193.113.8.102:80',
'189.203.10.116:999',
'177.73.112.63:9090',
'139.255.21.74:8080',
'52.27.65.162:80',
'207.180.224.75:80',
'197.254.97.255:80',
'5.180.130.91:443',
'212.95.75.12:80',
'62.205.169.74:53281',
'197.254.97.251:80',
'18.223.136.29:80',
'3.215.177.148:49205',
'88.255.102.98:8080',
'176.118.209.12:53281',
'201.249.161.51:999',
'203.207.52.206:8085',
'164.132.106.217:8087',
'212.115.232.79:31280',
'35.238.154.2:80',
'167.71.230.124:8080',
'202.61.204.51:80',
'78.189.32.215:8080',
'43.224.10.30:6666',
'146.196.40.109:8181',
'51.91.124.151:80',
'123.200.5.210:45780',
'202.61.254.57:8118',
'5.104.174.199:23500',
'150.109.32.166:80',
'49.204.87.252:80',
'186.250.23.153:3128',
'119.82.241.21:8080',
'177.73.112.66:9090',
'181.129.98.146:8080',
'190.110.111.148:999',
'190.186.1.121:999',
'190.14.224.244:999',
'41.60.236.155:8080',
'77.238.129.14:55443',
'138.201.154.35:24000',
'87.255.13.217:8080',
'80.191.162.2:514',
'177.8.113.63:50297',
'110.74.195.34:25',
'95.154.104.147:44393',
]