from django.utils.http import urlquote
from django.utils.encoding import iri_to_uri

query = 'Rh&ouml;l'
url_query = urlquote(query)
iri_query = iri_to_uri(query)
print url_query
print iri_query