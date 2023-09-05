from pathlib import Path

import scrapy

'''
이 파일 먼저 실행 후 get_bond_report_summary_spider.py 실행
작업 경로: ~/BOK_TEAM_2/bond_report_head
scrapy 라이브러리 설치 및 실행. # 붙은 것은 conda에서 실행
완료 후 아래 문서 read. sep(구분자)='\t\t\t'
total_report_summary.txt

# conda activate {env}
# pip install scrapy
# cd {경로}/BOK_TEAM_2/bond_report_head
# scrapy crawl get_urls_spider
# scrapy crawl get_bond_report_summary_spider 
'''

class QuotesSpider(scrapy.Spider):
    name = "get_urls_spider"

    def start_requests(self):
        base = 'https://finance.naver.com/research/debenture_list.naver?&page='
        urls = ['https://finance.naver.com/research/debenture_list.naver?&page='+str(i) for i in range(1,199)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        d = response.css('div.box_type_m table a::attr(href)').getall()
        with open('total_url.txt', 'a', encoding='utf_8') as f:
	        for _ in d:
                  if _.find('debenture_read')==0:
                    f.write('https://finance.naver.com/research/'+_+'\n')