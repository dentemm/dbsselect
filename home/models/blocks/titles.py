from wagtail.core.blocks import CharBlock

class TitleBlock(CharBlock):

    class Meta:
        template = 'home/blocks/title.html'
        icon = 'title'
        label = 'Titel'
