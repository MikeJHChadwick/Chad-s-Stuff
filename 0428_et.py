import xml.etree.ElementTree as ET
import re

tree= ET.parse('C:/Users/Learner_9ZH3Z126/2023_data_engineering/sammis_python_work/Chad\'s Stuff/movies.xml')
root= tree.getroot()
# print(root)
# print(root.tag)
# #attribute in xml is a name value pair
# print(root.attrib)


# for child in root:
#     print(child.tag, child.attrib)
#     for children in child:
#         print(children.tag, children.attrib)
#         for grandchild in children:
#             print(grandchild.tag, grandchild.attrib)
            
# print([elem.tag for elem in root.iter()])

# print(ET.tostring(root, encoding='utf8').decode('utf8'))


for movie in root.iter('movie'):
    print(movie.attrib, movie.text)
    
for description in root.iter('description'):
    print(description.text)
    
    
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/[rating ='R']"):
    print(movie.attrib)
    
    # the @ grabs all the elements of the tag grouped under format
    #the '@' is used for attributes; year is a node; multiple is an attribute within the node format
    #hence, [year = '1992'] vs [@multiple = 'Yes']
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    # the ... will return the parent of what we're calling, so instead of getting multiple yes' we get the titles of the movies and if they're favorites
    #and you can keep adding ... to go up additional layers
    print(movie.attrib)
    
    

# b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']") 
# print(b2tf)
# b2tf.attrib["title"]= "Back to the Future"  
# print(b2tf)
    
    
# for form in root.findall("./genre/decade/movie/format"):
#        match= re.search(',',form.text)
#        if match:
#             form.set('miltiple','Yes') 
#        else:
#             form.set('multiple', 'No')


# tree.write("movies.xml")

# tree = ET.parse("movies.xml")
# root = tree.getroot()

for form in root.findall("./genre/decade/movie/format"):
     print(form.attrib, form.text)
    
 
for decade in root.findall("./genre/decade"):
    print(decade.attrib) 
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')

for movie in root.findall("./genre/decade/movie/[year='2000']"):
     print(movie.attrib)
action= root.find("./genre[@category='Action']")
thriller= root.find("./genre[@category='Thriller']")
new_dec= ET.SubElement(action, 'decade') 
new_dec2= ET.SubElement(thriller, 'decade') 
new_dec.attrib["years"] = '2000s'
new_dec2.attrib["years"] = '2000s'
print(ET.tostring(action, encoding='utf8').decode('utf8'))
print(ET.tostring(thriller, encoding='utf8').decode('utf8'))



# xmen = root.find("./genre/decade/movie[@title='X-Men']")
# dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
# dec2000s.append(xmen)
# dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
# dec1990s.remove(xmen)
# print(ET.tostring(action, encoding='utf8').decode('utf8'))


aPsycho = root.find("./genre/decade/movie[@title='American Psycho']")
dec2000s = root.find("./genre[@category='Thriller']/decade[@years='2000s']")
dec2000s.append(aPsycho)
dec1980s = root.find("./genre[@category='Thriller']/decade[@years='1980s']")
dec1980s.remove(aPsycho)
print(ET.tostring(thriller, encoding='utf8').decode('utf8'))

tree.write("C:/Users/Learner_9ZH3Z126/2023_data_engineering/sammis_python_work/Chad\'s Stuff/movies.xml")

# 1980s to 2000s 