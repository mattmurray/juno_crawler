# -*- coding: utf-8 -*-
# import scrapy
from scrapy import Spider
from scrapy.http import Request
from juno_crawler.items import JunoCrawlerItem

class JunoSpider(Spider):
    name = "juno"
    allowed_domains = ["junodownload.com"]
    start_urls = ['http://www.junodownload.com/all/back-cat/releases/?music_product_type=single']

    def parse(self, response):
        next_page_url = response.xpath('//a[span[contains(@class, "glyphicon-arrow-right")]]/@href').extract_first()

        item = JunoCrawlerItem()

        releases = response.xpath('.//div[@class="productlist_widget_container"]')
        for release in releases:
            artist_text = release.xpath(
                './/div[@class="productlist_widget_product_artists"]/span[@class="jq_highlight pwrtext"]/descendant-or-self::*/text()')
            artist_list = []
            for artist in artist_text:
                artist_list.append(artist.extract())

            artist = ''.join(artist_list)
            item['artist'] = artist

            title = release.xpath(
                './/div[@class="productlist_widget_product_title"]/span[@class="jq_highlight pwrtext"]/a/text()').extract_first()
            item['title'] = title

            label = release.xpath(
                './/div[@class="productlist_widget_product_label"]/span[@class="jq_highlight pwrtext"]/a/text()').extract_first()
            item['label'] = label

            track_div = release.xpath('.//div[@class="productlist_widget_tracklist_left"]')
            for tracks in track_div:
                track_urls = tracks.xpath(
                    './/div[@class="productlist_widget_tracklist_row"]/a[@ua_action="play"]/@href').extract()
                track_name_list = tracks.xpath(
                    './/div[@class="productlist_widget_tracklist_row_text"]/span[@class="jq_highlight"]/text()').extract()
                track_names = []
                for tracks in track_name_list:
                    track = tracks.replace('\t','')
                    if len(track) >0:
                        track_names.append(track)

            tracks = list(zip(track_names, track_urls))
            item['tracks'] = tracks

            catalog_number = release.xpath(
                './/div[@class="productlist_widget_product_preview_buy"]/text()').extract_first()
            catalog_number = catalog_number.strip()
            item['catalog_number'] = catalog_number

            release_date = release.xpath(
                './/div[@class="productlist_widget_product_preview_buy"]/span/text()').extract_first()
            item['release_date'] = release_date

            genre = release.xpath(
                './/div[@class="productlist_widget_product_preview_buy"]/span/following-sibling::span/text()').extract_first()
            genre = genre.strip()
            item['genre'] = genre

            yield item

        yield Request(next_page_url)