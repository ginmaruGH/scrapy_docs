import scrapy
from scrapy.crawler import CrawlerProcess

# spider class
class HeadersCookies(scrapy.Spider):
    name = "headerscookies"

    url = "https://enldafevk2rhb.x.pipedream.net/"

    # custom headers
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ja,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
        "cache-control": "max-age=0",
        "if-modified-since": "Wed, 01 Apr 2020 23:15:20 GMT",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
    }

    raw_cookie = "_gcl_au=1.1.2053070165.1592979574; _ga=GA1.2.1180196223.1592979574; _gid=GA1.2.1504925251.1592979574; _lr_uf_-dhjtrz=a5956b98-e3b3-41d8-ab3a-3f9c182bd391; _hjid=ec0ef6a8-a0b1-431d-abe1-01397ae26645; ki_r=; _uetsid=11adf75b-e96c-d7d7-9ea2-dfa133728451; _uetvid=d6cd5e1d-cdde-40f2-01b6-f60ff4361f57; _gat_UA-128559955-1=1; _lr_tabs_-dhjtrz%2Fpd={%22sessionID%22:0%2C%22recordingID%22:%224-be179f28-1ed2-4d5d-81ff-e6d0d409ac9a%22%2C%22lastActivity%22:1592986151170}; _lr_hb_-dhjtrz%2Fpd={%22heartbeat%22:1592986151172}; ki_t=1592979575629%3B1592979575629%3B1592986152027%3B1%3B5; amplitude_id_eadd7e2135597c308ef5d9db3651c843requestbin.com=eyJkZXZpY2VJZCI6IjdjYTczN2U3LTkyMzMtNDllOC1iOGUxLTEwMGRiZGM1YWEwM1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Mjk4NTczNzcyNiwibGFzdEV2ZW50VGltZSI6MTU5Mjk4NjE1MjEyNywiZXZlbnRJZCI6NiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjZ9"

    # parse cookies
    def parse_cookies(self, raw_cookies):
        cookies = {}
        for cookie in raw_cookies.split('; '):
            try:
                key = cookie.split('=')[0]
                val = cookie.split('=')[1]
                cookies[key] = val
            except:
                pass

        return cookies

    def start_requests(self):
        # make HTTP GET request to requestbin.com
        yield scrapy.Request(
            url = self.url,
            headers = self.headers,
            cookies = self.parse_cookies(self.raw_cookie),
            callback = self.parse
        )

    def parse(self, response):
        print(response.text)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(HeadersCookies)
    process.start()
