from utils import plugins

from utils.install import update_settings

PLUGIN_NAME = 'Mailchimp Plugin'
DISPLAY_NAME = 'Mailchimp'
DESCRIPTION = 'A Mailchimp plugin for janeway.'
AUTHOR = 'Andy Byers'
VERSION = '0.1'
SHORT_NAME = 'mailchimp'
MANAGER_URL = 'mailchimp_manager'
JANEWAY_VERSION = "1.4.0"

API_KEY = ''
SERVER_PREFIX = ''
LIST_ID = ''


class MailchimpPlugin(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = DISPLAY_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME
    manager_url = MANAGER_URL

    version = VERSION
    janeway_version = JANEWAY_VERSION
    is_workflow_plugin = False


def install():
    MailchimpPlugin.install()


def hook_registry():
    MailchimpPlugin.hook_registry()


def register_for_events():
    pass
