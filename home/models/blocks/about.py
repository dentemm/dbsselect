from wagtail.core.blocks import CharBlock, TextBlock, StructBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock

class AboutBlock(StructBlock):

  title = CharBlock(label='titel', max_length=64)
  content = TextBlock(label='tekst', max_length=512)
  image = ImageChooserBlock(label='afbeelding', required=False)
  gallery = ListBlock(ImageChooserBlock(), label='foto gallerij', required=False)

  class Meta:
    template = 'home/blocks/about_block.html'
    icon = 'placeholder'
    label = 'inhoudsblok'