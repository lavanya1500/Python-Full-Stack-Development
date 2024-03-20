import json
from projectApp.models import MyModel
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help= 'Import external JSON file data into Django database'

    def handle(self,*args,**kwargs):
        json_path=r"C:\Users\Admin\Downloads\jsondata.json"
        with open(json_path,'r', encoding='utf-8') as f:
            data = json.load(f)

            for item in data:
                MyModel.objects.create(
                    end_year=item['end_year'],
                    intensity=item['intensity'],
                    sector=item['sector'],
                    topic=item['topic'],
                    insight=item['insight'],
                    url=item['url'],
                    region=item['region'],
                    start_year=item['start_year'],
                    impact=item['impact'],
                    added=item['added'],
                    published=item['published'],
                    country=item['country'],
                    relevance=item['relevance'],
                    pestle=item['pestle'],
                    source=item['source'],
                    title=item['title'],
                    likelihood=item['likelihood']
                )
            
        self.stdout.write(self.style.SUCCESS('Done'))