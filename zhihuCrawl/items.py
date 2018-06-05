# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihucrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #id
    user_id = scrapy.Field()
    #头像
    user_image_url = scrapy.Field()
    #姓名
    name = scrapy.Field()
    #居住地
    location = scrapy.Field()
    #技术领域
    business = scrapy.Field()
    #性别
    gender = scrapy.Field()
    #公司
    emploryment = scrapy.Field()
    #职位
    position = scrapy.Field()
    #教育经历
    education = scrapy.Field()
    #关注的人数
    fillowees_num = scrapy.Field()
    #关注我的人数
    followers_num = scrapy.Field()


class RelationItem(scrapy.Ttem):
    #用户ID
    user_id = scrapy.Field()
    #关系类型
    relation_type = scrapy.Field()
    #有关系的人的ID列表
    relation_id = scrapy.Field()
