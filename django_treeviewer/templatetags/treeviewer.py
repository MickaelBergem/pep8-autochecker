from django.core import serializers
from django.template import Library
from django.template import Context
from django.template.loader import get_template

register = Library()

# -------------------------
# Template Tags
# -------------------------


@register.filter
def render_tree(tree):
    """
    From a dict, returns the rendered tree
    """

    template = get_template("django_treeviewer/templates/tree.html")
    context = Context({'tree': tree})

    return template.render(context)
