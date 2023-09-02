from pathlib import Path

import scrapy, re

# get_urls_spider.py 먼저 확인. 사용법 등 기술.

class QuotesSpider(scrapy.Spider):
    name = "get_bond_report_summary_spider"

    def start_requests(self):
        with open('./total_url.txt', 'rb') as f:
            urls = f.read()
        # 바이너리 문자열로 변환
        urls = str(urls).replace('b\'','').split('\\r\\n')[:-1]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        custom_sep = '\t\t\t'   # 구분자 지정. 다른 데서 읽을 때 동일 str 기입.
        sbj = response.css('div.box_type_m table th.view_sbj::text').get().strip()+custom_sep
        company_name, date_, trash = response.css('div.box_type_m table p.source::text').getall()
        company_name+=custom_sep
        date_+=custom_sep
        headline = "None"+custom_sep
        context = "None\n"
        try:
            headline = response.css('div.box_type_m table td.view_cnt p strong::text').get()+custom_sep
        except:
            headline = response.css('div.box_type_m table *::text').getall()[1]+custom_sep
        context = ''.join(response.css('div.box_type_m table *::text').getall())
        context = re.sub(r'\n\t', ' ', context.replace('\xa0',' ').split('\n                ')[2]).strip().replace('  ', ' ')
        context = ' '.join(context.split())+'\n'
        
        res = response.url+custom_sep+sbj+company_name+date_+headline+context
        with open('total_report_summary.txt', 'a', encoding='utf_8') as f:
            f.write(res)