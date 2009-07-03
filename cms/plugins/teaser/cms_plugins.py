from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cms.settings import CMS_MEDIA_URL
from cms.plugins.teaser.models import Teaser

class TeaserPlugin(CMSPluginBase):
    model = Teaser
    name = _("Teaser")
    render_template = "cms/plugins/teaser.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'object':instance, 
            'placeholder':placeholder,
            'link':link
        })
        return context 
    
    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return CMS_MEDIA_URL + u"images/plugins/image.png"
 
plugin_pool.register_plugin(TeaserPlugin)