

def build_namespace(namespace, pattern_namespace):
    if namespace and pattern_namespace:
        return "%s:%s" % (namespace, pattern_namespace)
    else:
        return pattern_namespace or namespace or None

def get_patterns(urlpatterns, namespace=None):
    views = []
    for pattern in urlpatterns:
        if hasattr(pattern, 'url_patterns'):
            views += get_patterns(pattern.url_patterns, build_namespace(namespace, pattern.namespace))
        else:
            views.append((namespace, getattr(pattern, 'name', None), pattern.callback))
    return views

from urls import urlpatterns
all_patterns = get_patterns(urlpatterns)

from collections import defaultdict
grouped_urls = defaultdict(list)
for namespace, name, view_func in sorted(all_patterns):
    if namespace and ':' in namespace:
        key = namespace[0:namespace.index(':')]
    else:
        key = namespace
    grouped_urls[key].append((namespace, name, view_func))

quote_urls = len(grouped_urls['quote'])
assert quote_urls  == 26, "%s => %s" % (quote_urls, grouped_urls['quote'])

quoteoptions_urls = len(grouped_urls['quote_options'])
assert quoteoptions_urls == 61, grouped_urls['quote_options']

main_urls = len(grouped_urls['main'])
assert main_urls == 28, grouped_urls['main']

reports_urls = len(grouped_urls['reports'])
assert reports_urls == 14, grouped_urls['reports']

navigator_urls = len(grouped_urls['navigator'])
assert navigator_urls == 16, grouped_urls['navigator']

assert len(grouped_urls['dashboard']) == 8
assert len(grouped_urls['appsfiles']) == 5
assert len(grouped_urls['cpanel']) == 24

assert len(grouped_urls['mutual']) == 5
assert len(grouped_urls['services']) == 5 + 2 + 5, len(grouped_urls['services'])
assert len(grouped_urls['user_settings']) == 3

#done
