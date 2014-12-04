from conceptmap import ConceptNetCollector

collector = ConceptNetCollector()
#conceptMap = collector.makeConceptMap('cold', 'ReceivesAction')
#collector.printRelations('naked truth')
#biting is a "VBG, gerund present/participle"
#cold is an NN
#Cold hasProperty Biting
#for k, v in conceptMap.items():
#    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v)))
conceptMap = collector.makeConceptMap('forward', 'HasProperty')
for k, v in conceptMap.items():
    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v)))   
conceptMap = collector.makeConceptMap('momentum', 'HasProperty')
for k, v in conceptMap.items():
    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v)))  

collector.printRelations('forward momentum') 
print("---------------------")
conceptMap = collector.makeConceptMap('cold', 'IsA')
#for k, v in conceptMap.items():
#    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v)))  
conceptMap = collector.makeConceptMap('biting', 'CapableOf')
#for k, v in conceptMap.items():
#    print("key %s val %s" % (collector.stripUri(k), collector.stripUri(v))) 
#print(conceptMap)
#collector.printRelations('break')
print(collector.getAssociations('liquid', 'value').result)
resultDict = collector.getAssociations('liquid', 'value').result
resultScore = 0
for assoc, item in resultDict.items():
    if item and item[0] and len(item[0]) > 1:
        if assoc == 'similar':
            for score in item:
                print(score[1])
            resultScore += item[0][1]  


