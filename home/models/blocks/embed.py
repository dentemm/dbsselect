from wagtail.embeds.blocks import EmbedBlock

class CustomEmbedBlock(EmbedBlock):

    class Meta:
        template = 'home/blocks/embed.html'
        icon = 'media'
        label = 'Video Embed'