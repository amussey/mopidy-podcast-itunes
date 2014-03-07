from __future__ import unicode_literals

from mopidy import config, ext

__version__ = '0.0.1'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Podcast-iTunes'
    ext_name = 'podcast-itunes'
    version = __version__

    def get_default_config(self):
        import os
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['browse_label'] = config.String()
        return schema

    def setup(self, registry):
        from .directory import ITunesDirectory
        registry.add('podcast:directory', ITunesDirectory)
