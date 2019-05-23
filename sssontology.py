from rdflib import RDFS, RDF, Namespace, Graph, URIRef
class sssontology(object):
    def __init__(self,filename='ssso_v1.ttl'):
        self.filename=filename
        self.g = Graph()
        self.g.parse(self.filename, format='turtle')
        ssso = Namespace('http://www.semanticweb.org/linch/ontologies/2018/11/ssso#')
        self.g.bind('ssso', ssso)
        self.g.bind('rdf', RDF)
        self.m = {
        'http://www.w3.org/1999/02/22-rdf-syntax-ns': 'rdf',
        'http://www.semanticweb.org/linch/ontologies/2018/11/ssso':'ssso'
        }
    def refresh(self):
        self.g = Graph()
        self.g.parse(self.filename, format='turtle')
    def commit(self):
        self.g.serialize(destination=self.filename, format='turtle')
    def add(self,triple):
        self.g.add(triple)
        self.g.serialize(destination=self.filename, format='turtle')
    def remove(self,triple):
        self.g.remove(triple)
        self.g.serialize(destination=self.filename, format='turtle')
    def query(self,q,fullURI=False):
        query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>PREFIX ssso: <http://www.semanticweb.org/linch/ontologies/2018/11/ssso#>"""+q
        rows = self.g.query(q)
        if not fullURI:
            rows = [[self.m[r.split('#')[0]] + ':' + r.split('#')[1] if isinstance(r, URIRef) and '#' in r else r for r in row] for row in rows]
            return rows
        return list(rows)