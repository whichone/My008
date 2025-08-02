"""A short description of the project"""

from plugin import InvenTreePlugin

from plugin.mixins import SettingsMixin, UserInterfaceMixin, AppMixin

from . import PLUGIN_VERSION

from django.apps import AppConfig

class My008App(AppMixin, AppConfig):
    name = "my008"  # This must match the Python module (folder) name
    label = "my008"  # Optional but recommended: ensures unique app label

class My008(SettingsMixin, UserInterfaceMixin, InvenTreePlugin):

    """My008 - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "My008"
    NAME = "My008"
    SLUG = "my008"
    DESCRIPTION = "A short description of the project"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "John Doe"
    WEBSITE = "https://my-project-url.com"
    LICENSE = "MIT"
    APP = My008App
    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'

    
    
    
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    
    
    
    
    

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/ui/
    
    # Custom UI panels
    def get_ui_panels(self, request, context: dict, **kwargs):
        """Return a list of custom panels to be rendered in the InvenTree user interface."""

        panels = []

        # Only display this panel for the 'part' target
        if context.get('target_model') == 'part':
            panels.append({
                'key': 'my008-panel',
                'title': 'My008',
                'description': 'Custom panel description',
                'icon': 'ti:mood-smile:outline',
                'source': self.plugin_static_file('Panel.js:renderMy008Panel'),
                'context': {
                    # Provide additional context data to the panel
                    'settings': self.get_settings_dict(),
                    'foo': 'bar'
                }
            })
        
        return panels
    

    
