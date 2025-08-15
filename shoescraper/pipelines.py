# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ShoescraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
    
        #normalized data
        #Strip whitespace & set it to float on size lists
        size_lists = adapter.get('size_lists')
        print("*******************************")
        print(size_lists)
        trimmed = [trim.strip() for trim in size_lists[0]] 
        float_trimmed = [float(f) for f in trimmed]
        print(float_trimmed)
        adapter['size_lists'] = float_trimmed
        return item
