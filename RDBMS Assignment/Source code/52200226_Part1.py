# Import tabulate module for writing data in specified format
from tabulate import tabulate

# Open file input1.txt in read text mode
file = open('input1.txt', 'rt')

# Create empty dictionary to store all of entities and its attributes
entity_dic = {}

# Create empty list to store all of relationships between entities
relationship_list  = []

# Read line of file in sequence
for line in file:
    
    lst = line.split() # split line into list by space seperator
    
    # If it is entity then store its attribute
    if len(lst) == 2:
        # Retrieve name of entity
        entity_name = lst[0]

        # Retrieve attribute part without brackets
        attribute = lst[1][1: len(lst[1]) - 1].split(',')

        # Add to dictionary
        entity_dic[entity_name] = attribute
    
    # If it is relationship then processing
    elif len(lst) == 3:

        # Retrieve two entities joining in relationship
        entity1 = lst[0]
        entity2 = lst[2]

        # Retrieve the relationship between two entities
        relationship = lst[1]

        # If the relationship is 1-N 
        if relationship == '1-N':

            # Then move PK of entity1 into FK in entity2
            entity1_PK = entity_dic.get(entity1)[0]
            entity2_FK = entity1_PK[0:len(entity1_PK) - 3] + '-FK'
            entity_dic[entity2].append(entity2_FK)

            # Add relationship into list of combination relationship
            relationship_list.append((lst[0] + ' ' + lst[1] + ' ' + lst[2]).split())

        # If relationship is N-N:
        elif 'N-N' in relationship:
            
            # Retrieve new entity's name
            new_entity = relationship[4: len(relationship) - 1]
            
            # Get new primary key of the two enities
            # It's foreign key as well 
            new_PK_FK1 = entity_dic.get(entity1)[0] + '-FK'
            new_PK_FK2 = entity_dic.get(entity2)[0] + '-FK'
            
            # If new entity doesnt has its attribute then create empty list
            if new_entity not in entity_dic:
                entity_dic[new_entity] = []

            # Add them into new enity's attribute
            entity_dic[new_entity].insert(0, new_PK_FK1)
            entity_dic[new_entity].insert(1, new_PK_FK2)

            # Add relationship into list of combination relationship
            relationship_list.append((lst[0] + ' ' + 'N-N' + ' ' + lst[2]).split())
            relationship_list.append((lst[0] + ' ' + '1-N' + ' ' + new_entity).split())
            relationship_list.append((lst[2] + ' ' + '1-N' + ' ' + new_entity).split())

        # If relationship is 1-1:
        elif relationship == '1-1':

            # Retrive one primary in whether entity1 or entity2
            entity2_PK = entity_dic.get(entity2)[0]

            # And add it into entity1 as foreign key
            entity1_new_FK = entity2_PK[0: len(entity2_PK) - 3] + '-FK'
            entity_dic[entity1].append(entity1_new_FK)

            # Add relationship into list of combination relationship
            relationship_list.append((lst[0] + ' ' + lst[1] + ' ' + lst[2]).split())

        # If relationship is MANH-YEU:
        elif relationship == 'MANH-YEU':
            # Retrieve primary key of strong entity
            # Add it into weak entity, it is foreign key as well
            weak_entity_PK_FK = entity_dic.get(entity1)[0] + '-FK'
            entity_dic[entity2].insert(0, weak_entity_PK_FK)
            
            # Add relationship into list of combination relationship
            relationship_list.append((lst[0] + ' ' + '1-N' + ' ' + lst[2]).split())

        # If relationship is CHA-CON
        elif relationship == 'CHA-CON':

            # Retrieve primary of parent and add into child
            # It's foreign key as well
            parent_attribute = entity_dic.get(entity1)
            child_PK_FK = parent_attribute[0] + '-FK'
            entity_dic[entity2].insert(0, child_PK_FK)

            # Retrieve inherit attribute from parent
            inheritance_attribute = entity_dic.get(entity1)[1: len(parent_attribute)]
            
            # And add it into child
            for i in range(0, len(inheritance_attribute)):
                entity_dic[entity2].insert(i + 1, inheritance_attribute[i])

            # Add relationship into list of combination relationship
            relationship_list.append((lst[0] + ' ' + '1-1' + ' ' + lst[2]).split())

# Close file after finished reading   
file.close()

# Write data to output file
output = open('output1.txt', 'w', encoding = 'utf-8')

output.write(tabulate(entity_dic, headers = 'keys', tablefmt = 'simple_outline'))
output.write('\n\n')

output.write(tabulate(relationship_list, headers = ['TABLE', 'RELATIONSHIP', 'TABLE'], tablefmt = 'simple_grid'))
output.write('\n\n')

# Close ouput file
output.close()

