import re

import feedparser

from django import template

register = template.Library()

@register.tag(name='election_rss')
def do_rss_latest(parser, token):
    """
    A template tag to grab the latest articles from a given feed.
    The first argument is the category.
    The second argument is the number of items to retrieve.
    The third argument (after 'as') is the variable to store the result in.
    """

    try:
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires three arguments:"
            + "category, number of items to retrieve and a variable name"
            % token.contents.split()[0]
        )
    m = re.search(r'(.*?) ([0-9]+) as (\w+)', args)

    if not m:
        raise template.TemplateSyntaxError(
            "%r has invalid arguments" % tag_name
        )

    category, num_items, var_name = m.groups()

    #if not (category[0] == category[-1]
    #        and category[0] in ('"', "'")):
    #    raise template.TemplateSyntaxError(
    #        "%r's category argument must be in quotes" % tag_name
    #    )
    try:
        number_of_items = int(num_items)
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r's second argument must be a number" % tag_name
        )
    return GetRSSLatest(category, number_of_items, var_name)


class GetRSSLatest(template.Node):
    def __init__(self, category, number_of_items, var_name):
        self.category = template.Variable(category)
        self.number_of_items = number_of_items
        self.var_name = var_name

    def render(self, context):
        try:
            actual_category = self.category.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        context[self.var_name] = []
        feed_url = 'http://blogs.seattletimes.com/politicsnorthwest/category/'
        feed_url += str(actual_category)
        feed_url += '/feed/'
        d = feedparser.parse(feed_url)
        for item in d.entries[:self.number_of_items]:
            try:
                rss_item = {
                    'title': item.title_detail['value'],
                    'href': item.link,
                }
                context[self.var_name].append(rss_item)
            except AttributeError:
                pass
        return ''

