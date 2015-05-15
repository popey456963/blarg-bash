from lxml import etree
api = API(locale='EN')
results = api.call(Operation='...') # your API call
print etree.tostring(results, pretty_print=True)