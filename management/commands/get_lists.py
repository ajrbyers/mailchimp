from django.core.management.base import BaseCommand

from plugins.mailchimp import plugin_settings

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = MailchimpMarketing.Client()
        client.set_config({
            "api_key": plugin_settings.API_KEY,
            "server": plugin_settings.SERVER_PREFIX
        })
        response = client.lists.get_all_lists()
        lists = (response.get('lists'))

        for list in lists:
            print(list.get('id'))