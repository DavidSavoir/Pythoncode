teachersdict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
  'Kenneth Love': ['Python Basics', 'Python Collections']}


def most_classes(teachers):
    max_count = 0
    namelist = {}
#for value in teachers.values():
    for name, value in teachersdict.items():
        print (value)
        for values in value:
            print (values)
            max_count += 1

        namelist[name] = max_count
        max_count = 0

    return(max(namelist, key=namelist.get))

def num_teachers(namelist):
  namelist = {}
  name_count = 0
  for name in teachersdict.items():
    name_count += 1
  return (name_count)

most_classes(teachersdict)

num_teachers(most_classes)

def stats(teachersd):
    max_count = 0
    namelist = []
    for name, value in teachersdict.items():
        print (value)
        for values in value:
            print (values)
            max_count += 1
        namelist.append([name, max_count])
        max_count = 0
    #return (namelist)
    newnamelist = [item for sublist in namelist for item in sublist]
    return (newnamelist)
