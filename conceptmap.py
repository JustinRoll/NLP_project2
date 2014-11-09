from conceptnet5_client.utils.debug import print_debug
from conceptnet5_client.utils.http import make_http_request
from conceptnet5_client.utils.util import is_arg_valid
from conceptnet5_client.utils.result import Result
from conceptnet5_client.conf import settings
from conceptnet5_client.web.api import LookUp

class ConceptNetCollector:

    def getConceptUri(self, concept):
        return '/c/en/%s' % concept

    def getRelationUri(self, relation):
        return '/r/%s' % relation

    def stripUri(self, uri):
        uri = uri.replace('/r/', '')
        uri = uri.replace('/c/en/', '')
        return uri

    def printRelations(self, term):
        lookup = LookUp(limit=500)
        response = lookup.search_concept(term)
        response = Result(response)
        edges = response.parse_all_edges(clean_self_ref = True)

        for edge in edges:
            print("%s --> %s --> %s" % (edge.start, edge.rel, edge.end))

    def makeConceptMap(self, term, modifier):
        lookup = LookUp(limit=500)
        response = lookup.search_concept(term)
        response = Result(response)
        edges = response.parse_all_edges(clean_self_ref = True)

        conceptMap = {}
        for edge in edges:
            if edge.rel == self.getRelationUri(modifier):
                conceptMap[edge.start] = edge.end
        return conceptMap
