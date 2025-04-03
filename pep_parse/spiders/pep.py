import scrapy
import re

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        yield response.follow("numerical/", callback=self.parse_numerical)

    def parse_numerical(self, response):
        index = response.xpath('//*[@id="numerical-index"]').css("tbody")
        all_hrefs = index.css("a::attr(href)").getall()
        for href in all_hrefs:
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит страницы с документами и формирует Items"""
        pep = response.css("section[id='pep-content']")
        pattern = re.compile(r"^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)")
        h1_tag = pattern.search(pep.css("h1::text").get())
        if h1_tag:
            number, name = h1_tag.group("number", "name")
        context = {
            "number": number,
            "name": name,
            "status": pep.css("abbr::text").get(),
        }
        yield PepParseItem(context)
