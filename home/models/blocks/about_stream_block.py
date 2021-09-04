from wagtail.core.blocks import StreamBlock

from .about import AboutBlock

class AboutPageStreamBlock(StreamBlock):
  content = AboutBlock()