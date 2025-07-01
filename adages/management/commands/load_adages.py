import json
from adages.models import Adage
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Loads adages from a json file into the database.'

    def add_arguments(self,parser):
        parser.add_argument('--filename',type=str,help='Enter name of json file with adages')

    def handle(self, *args,**options):
        filename=options['filename']
        with open(filename) as f:
            adages = json.load(f)
        for adage in adages:
            adage_id = adage["id"]
            adage_text = adage["adage_text"]
            adage_meaning = adage["adage_meaning"]
            review_status = False

            try:
                # look for existing adage by name
                adage_obj = Adage.objects.get(adage_text=adage_text)

                # update the description if the adage exits
                adage_obj.adage_meaning= adage_meaning
                adage_obj.adage_id = adage_id
                adage_obj.review_status = review_status
                adage_obj.save()
            except Adage.DoesNotExist:
                # create a new adage if it does not exist
                Adage.objects.create(adage_id=adage_id,adage_text=adage_text,adage_meaning=adage_meaning,review_status=review_status)
        self.stdout.write(self.style.SUCCESS("Adages loaded successfully."))
