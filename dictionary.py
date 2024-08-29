#dictionary in python

capitals = {'usa':'washington DC',
            'China':'Beijing',
            'india':'New Dehli',
            'Russia':'Moscow'}


capitals.update({'Germany':'Berlin'})
capitals.update({'Usa':'Las vegas'})
capitals.pop('China')
capitals.clear()



#print(capitals['Russia'])
#print(capitals.get('germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)