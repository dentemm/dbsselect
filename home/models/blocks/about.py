from wagtail.core.blocks import CharBlock, TextBlock, StructBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock

class AboutBlock(StructBlock):

  title = CharBlock(max_length=64)
  content = TextBlock(max_length=512)
  image = ImageChooserBlock(required=False)
  gallery = ListBlock(ImageChooserBlock, required=False)

  class Meta:
    template = 'home/blocks/about.html'
    icon = 'placeholder'
    label = 'About block'