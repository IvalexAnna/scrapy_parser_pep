import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import NAME, START_URLS, ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    name = NAME
    start_urls = START_URLS
    allowed_domains = ALLOWED_DOMAINS

    def parse(self, response):
        yield response.follow("numerical/", callback=self.parse_numerical)

    def parse_numerical(self, response):
        index = response.xpath('//*[@id="numerical-index"]').css("tbody")
        all_hrefs = index.css("a::attr(href)").getall()
        for href in all_hrefs:
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        pep = response.css("section[id='pep-content']")
        h1_tag = pep.css("h1::text").get()
        h1_tag = h1_tag.replace('–', '')
        parts = h1_tag.split()
        number = None
        name = None

        for i, part in enumerate(parts):
            if part.startswith("PEP"):
                number = parts[i + 1]
                name = ' '.join(parts[i + 2:])
                break

        context = {
            "number": number,
            "name": name,
            "status": pep.css("abbr::text").get(),
        }

        yield PepParseItem(context)
