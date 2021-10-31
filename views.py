import json

from django.shortcuts import render, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from plugins.mailchimp import plugin_settings

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


@staff_member_required
def manager(request):
    pass


def signup(request):
    api_error = None
    if request.POST:
        client = MailchimpMarketing.Client()
        client.set_config({
            "api_key": plugin_settings.API_KEY,
            "server": plugin_settings.SERVER_PREFIX
        })

        member_info = {
            "email_address": request.user.email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": request.user.first_name,
                "LNAME": request.user.last_name,
            }
        }

        kwargs = {"skip_merge_validation": False}

        try:
            response = client.lists.add_list_member(plugin_settings.LIST_ID, member_info, **kwargs)
            print("response: {}".format(response))
            messages.add_message(
                request,
                messages.SUCCESS,
                'You have been signed up.',
            )
            return redirect(
                reverse(
                    'website_index',
                )
            )
        except ApiClientError as error:
            error_dict = json.loads(error.text)
            if error_dict.get('title') == 'Member Exists':
                api_error = 'You are already subscribed.'
            else:
                api_error = 'An unspecified error occurred.'

    template = 'mailchimp/signup.html'
    context = {
        'api_error': api_error,
    }

    return render(request, template, context)
