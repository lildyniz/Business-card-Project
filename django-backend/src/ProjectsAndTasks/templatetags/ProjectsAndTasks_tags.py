from django import template


register = template.Library()

# import markdown
# @register.filter(name='render_markdown')
# def render_markdown(text):
#     return markdown.markdown(text)

# pip install markdown2[all]
import markdown2
@register.filter(name='render_markdown')
def render_markdown(text):
    return markdown2.markdown(text, extras=['fenced-code-blocks'])