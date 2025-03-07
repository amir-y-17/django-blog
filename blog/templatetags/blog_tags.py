from django import template
from ..models import Post


register = template.Library()


@register.inclusion_tag("parent/partials/latest_posts.html")
def latest_posts(count=4):
    l_posts = Post.objects.order_by("-created_at")[:count]
    context = {"l_posts": l_posts}
    return context
