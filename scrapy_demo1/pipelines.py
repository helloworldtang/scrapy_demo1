# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql

class ScrapyDemo1Pipeline(object):
    def __init__(self) -> None:
        super().__init__()

        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='python-local-test',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)


    def process_item(self, item, spider):
        print("item:", item)
        with self.conn.cursor() as cursor:
            print("begin persist")
            # Create a new record
            sql = "insert into pipeline_mysql(title,meta) values(%s,%s)"
            cursor.execute(sql, (item['urlTitle'], item['urlMeta']))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
        self.conn.commit()
        return item


# http://scrapy.readthedocs.io/en/latest/topics/item-pipeline.html#topics-item-pipeline
class MongoPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict[item])
        return item
