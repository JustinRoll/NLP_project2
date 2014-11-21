from conceptmap import ConceptNetCollector

collector = ConceptNetCollector()
#conceptMap = collector.makeConceptMap('cold', 'ReceivesAction')
collector.printRelations('naked truth')
#biting is a "VBG, gerund present/participle"
#cold is an NN
#Cold hasProperty Biting
#for k, v in conceptMap.items():
#    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v)))
conceptMap = collector.makeConceptMap('cold', 'HasProperty')
#for k, v in conceptMap.items():
#    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v)))  
print("---------------------")
conceptMap = collector.makeConceptMap('cold', 'IsA')
#for k, v in conceptMap.items():
#    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v)))  
conceptMap = collector.makeConceptMap('biting', 'CapableOf')
#for k, v in conceptMap.items():
#    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v))) 
#print(conceptMap)
#collector.printRelations('break')
conceptMap = collector.makeConceptMap('break', 'CapableOf')
collector.getAssociations('broken', 'glass')

