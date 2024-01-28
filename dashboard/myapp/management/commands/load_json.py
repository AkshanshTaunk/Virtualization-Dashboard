from datetime import datetime
from django.core.management.base import BaseCommand
import json
from myapp.models import DashboardData


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("dashboard\data\jsondata.json", "r", encoding='utf-8') as file:
            load_data = json.load(file)

        print(load_data)
        bulk_data = [DashboardData(
            end_year = data["end_year"],
            intensity = data["intensity"] if data["intensity"] !="" else None,
            sector = data["sector"],
            topic = data["topic"],
            insight = data["insight"],
            url = data["url"],
            region = data["region"],
            start_year = data["start_year"],
            impact = data["impact"],
            added = data["added"],
            published = data["published"],
            country = data["country"],
            relevance = data["relevance"] if data["relevance"] !="" else None,
            pestle = data["pestle"],
            source = data["source"],
            title = data["title"],
            likelihood = data["likelihood"] if data["likelihood"] !="" else None,
        ) for data in load_data]
        DashboardData.objects.bulk_create(bulk_data)
        print("Data created succesfully")