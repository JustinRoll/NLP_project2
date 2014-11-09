from conceptmap import ConceptNetCollector

collector = ConceptNetCollector()
conceptMap = collector.makeConceptMap('cold', 'ReceivesAction')
print(conceptMap)
print("---------------------")
conceptMap = collector.makeConceptMap('biting', 'CapableOf')
print(conceptMap)
#printRelations('break')
conceptMap = collector.makeConceptMap('break', 'CapableOf')
print(conceptMap)

