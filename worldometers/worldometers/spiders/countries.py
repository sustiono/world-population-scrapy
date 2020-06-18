# -*- coding: utf-8 -*-
import logging

import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath('//td/a')
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()
            yield response.follow(url=link, callback=self.parse_detail, meta={'country_name': name})

    def parse_detail(self, response):
        country_name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            yield {
                'country_name': country_name,
                'year': row.xpath('.//td[1]/text()').get(),
                'population': row.xpath('.//td[2]/strong/text()').get(),
                'yearly_change_in_percent': row.xpath('.//td[3]/text()').get(),
                'yearly_change_in_number': row.xpath('.//td[4]/text()').get(),
                'migrants': row.xpath('.//td[5]/text()').get(),
                'median_age': row.xpath('.//td[6]/text()').get(),
                'fertility_rate': row.xpath('.//td[7]/text()').get(),
                'dencity': row.xpath('.//td[8]/text()').get(),
                'urban_population_in_perecent': row.xpath('.//td[9]/text()').get(),
                'urban_population_in_number': row.xpath('.//td[10]/text()').get(),
                'world_population_in_percent': row.xpath('.//td[11]/text()').get(),
                'world_population_in_number': row.xpath('.//td[12]/text()').get(),
                'global_rank': row.xpath('.//td[13]/text()').get()
            }