import sys
import csv
import collections
  

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  severity = collections.Counter()
  with open(r'C:\program1\suc_ph.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
      severity[row[0]] +=1
  associations = severity.items()
  associations = sorted(associations, key=lambda pair: pair[1], reverse=True)
  sucph = associations[0][0]
  print "1. The region with the most SUC is " + sucph

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  i, count, y = 0, 0, 0
  regions = []
  reg = []
  with open('C:\program1\suc_ph.csv', 'rb') as F:
    read = csv.reader(F, delimiter=',')
    for row in read:
      reg.append(row[1])
  if school_year == '2010-2011':
    with open('C:\program1\suc_ph.csv', 'rb') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        regions.append(row[2])
  if school_year == '2011-2012':
    with open('C:\program1\suc_ph.csv', 'rb') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        regions.append(row[3])
  if school_year == '2012-2013':
    with open('C:\program1\suc_ph.csv', 'rb') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        regions.append(row[4])
  
  while i<len(regions):
    if regions[i].isdigit() :
      regions[i] = int(regions[i])

    else:
      regions[i] = 0
    i +=1
  enrol10 =  sorted(regions, key=int, reverse=True)
  for x in regions:
    if enrol10[0] == regions[y]:
      count = x
      break
    y +=1

  highest = reg[y]
  print "2. The region with the most SUC enrollees is " + highest

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  i, count, y = 0, 0, 0
  regions = []
  reg = []
  with open('C:\program1\suc_ph.csv', 'rb') as F:
    read = csv.reader(F, delimiter=',')
    for row in read:
      reg.append(row[1])
  if school_year == '2009-2010':
    with open('C:\program1\suc_ph.csv', 'rb') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        regions.append(row[5])
  if school_year == '2010-2011':
    with open('C:\program1\suc_ph.csv', 'rb') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        regions.append(row[6])
  if school_year == '2011-2012':
    with open('C:\program1\suc_ph.csv', 'rb') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        regions.append(row[7])
  
  while i<len(regions):
    if regions[i].isdigit() :
      regions[i] = int(regions[i])

    else:
      regions[i] = 0
    i +=1
  enrol10 =  sorted(regions, key=int, reverse=True)
  for x in regions:
    if enrol10[0] == regions[y]:
      count = x
      break
    y +=1

  highest = reg[y]
 
  print "3. The region with the most SUC graduates is " + highest


#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):

  a, b, c, d, x, y, z = 0, 0, 0, 0, 0, 0, 0
  tuition = []
  suc = []
  with open('C:\program1\sucfeeperunit.csv', 'rb') as F:
    read = csv.reader(F, delimiter=',')
    for row in read:
      suc.append(row[1])
  if school_year == '2010-2011':
    if level == 'BS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[2])
    if level == 'MS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[3])
    if level == 'PHD':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[4])
  if school_year == '2011-2012':
    if level == 'BS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[5])
    if level == 'MS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[6])
    if level == 'PHD':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[7])
  if school_year == '2012-2013':
    if level == 'BS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[8])
    if level == 'MS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[9])
    if level == 'PHD':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[10])
  while x<len(tuition):
    if tuition[x].isdigit() :
      tuition[x] = int(tuition[x])

    elif tuition[x] == 'free tuition fee':
      tuition[x] = 0
    else :
      tuition[x] = 10000
    x +=1
  fee =  sorted(tuition, key=int)
  for z in tuition:
    if fee[0] == tuition[a]:
      b = a
      
    if fee[1] == tuition[a]:
      c = a
      
    if fee[2] == tuition[a]:
      d = a
    a +=1

  top_1 = suc[b]
  top_2 = suc[c]
  top_3 = suc[d]
  print "4. Top 3 cheapest SUC for " + level + ' in school year ' + school_year
  print "  1." + top_1
  print "  2." + top_2
  print "  3." + top_3

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  a, b, c, d, x, y, z = 0, 0, 0, 0, 0, 0, 0
  tuition = []
  suc = []
  with open('C:\program1\sucfeeperunit.csv', 'rb') as F:
    read = csv.reader(F, delimiter=',')
    for row in read:
      suc.append(row[1])
  if school_year == '2010-2011':
    if level == 'BS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[2])
    if level == 'MS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[3])
    if level == 'PHD':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[4])
  if school_year == '2011-2012':
    if level == 'BS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[5])
    if level == 'MS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[6])
    if level == 'PHD':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[7])
  if school_year == '2012-2013':
    if level == 'BS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[8])
    if level == 'MS':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[9])
    if level == 'PHD':
      with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
          tuition.append(row[10])
  while x<len(tuition):
    if tuition[x].isdigit() :
      tuition[x] = int(tuition[x])
    else :
      tuition[x] = 0
    x +=1
  fee =  sorted(tuition, key=int, reverse=True)
  for z in tuition:
    if fee[0] == tuition[a]:
      b = a
      
    if fee[1] == tuition[a]:
      c = a
      
    if fee[2] == tuition[a]:
      d = a
    a +=1

  top_1 = suc[b]
  top_2 = suc[c]
  top_3 = suc[d]
  
  print "5. Top 3 expensive SUC for " + level + ' in school year ' + school_year
  print "  1." + top_1
  print "  2." + top_2
  print "  3." + top_3


#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  a, b, c, d, x, y, z = 0, 0, 0, 0, 0, 0, 0
  tuition_2010 = []
  tuition_2013 = []
  suc = []
  with open('C:\program1\sucfeeperunit.csv', 'rb') as F:
    read = csv.reader(F, delimiter=',')
    for row in read:
      suc.append(row[1])
  with open('C:\program1\sucfeeperunit.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
      tuition_2010.append(row[2])
  with open('C:\program1\sucfeeperunit.csv', 'rb') as fi:
    readers = csv.reader(fi, delimiter=',')
    for row in readers:
      tuition_2013.append(row[8])
  while x<len(tuition_2010):
    if tuition_2010[x].isdigit() :
      tuition_2010[x] = int(tuition_2010[x])
    else :
      tuition_2010[x] = 0
    x +=1
  while z<len(tuition_2013):
    if tuition_2013[z].isdigit() :
      tuition_2013[z] = int(tuition_2013[z])
    elif tuition_2013[z] == '-':
      tuition_2013[z] = tuition_2010[z]
    else :
      tuition_2013[z] = 0
    z +=1
  final = []
  for y in range(0, len(tuition_2013)):
    if tuition_2010[y] < tuition_2013[y]:
      a = y
      final.append(a)
  allsuc = []
  for x in range(0, len(final)):
    allsuc.append(suc[final[x]])
  #print final

  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  for i in allsuc:
    print "      - " + i

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  a, b, c, d, e, f = 0, -1, 0, 0, 0, 0
  discipline = []
  grade = []
  rownum = 0;
  with open('C:\program1\sucperf.csv', 'rb') as F:
    read = csv.reader(F, delimiter=',')
    for row in read:
      #if row[2].strip().upper() != "TOTAL" and row[2].strip().upper() != "DISCIPLINE":
      discipline.append(row[2].strip())

  if school_year == '2010':
    rownum = 3

  if school_year == '2011':
    rownum = 4

  if school_year == '2012':
    rownum = 5

  with open('C:\program1\sucperf.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:

      if row[rownum].isdigit() :
        row[rownum] = int(row[rownum])
      else :
        row[rownum] = 0
      grade.append(row[rownum])

  # get unique values in discipline
  once = []
  for occur in discipline:
    if occur not in once:
      once.append(occur)


  total = []
  data=[]
  sample = {}
  str = ''
  for x in range(1, len(once)):
    str = once[x]
    indices = [i for i, y in enumerate(discipline) if y == once[x]]
    sample[str] = indices
    #data.append(indices)   #index of each discipline groupeds

  total_passer = {}
  for a in once:
    gradesum = 0

    if a.upper() != "TOTAL" and a.upper() != "DISCIPLINE" and a != "-":
      for grd in sample[a]:
        #if a in total_passer:
        #  gradesum = total_passer[a]
        #else:
        #  gradesum = 0

        gradesum += grade[grd]
      
      total_passer[a] = gradesum

  #print total_passer
  associations = total_passer.items();
  associations = sorted(associations, key=lambda pair: pair[1], reverse=True)
  #print associations


  m, n = 0, 0
  array=[]
  try:
    for x in range(0, 142) :
      values = [y for i, y in enumerate(data)]
      total.append(values)
    
  except IndexError:
    pass
  #print data[0]
  #print len(array)

  
 # for x in range(0, 143):))))
  #  while 
  #for y in range (2, len(once)):
   # if once[y] == discipline[d]:
    #  data.append(passer[d])
    #d  +=1
    #f = sum(data)
  #total.append(f)
 # print total
  #print data
  
  highest = associations[0][0]
  print "7. The discipline which has the highest passing rate is " + highest

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(subject, school_year):
  a, b, c, d, e, f = 0, -1, 0, 0, 0, 0
  discipline = []
  grade = {}
  rownum = 0;
  total = []
  data=[]
  sample = {}
  suc = {}
  xstr = ''
  rowctr =0

  if school_year == '2010':
    rownum = 3

  if school_year == '2011':
    rownum = 4

  if school_year == '2012':
    rownum = 5

  with open('C:\program1\sucperf.csv', 'rb') as F:
    read = csv.reader(F, delimiter=',')
    for row in read:
       discipline.append(row[1].strip())

  with open('C:\program1\sucperf.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:

      if row[rownum].isdigit() :
        row[rownum] = int(row[rownum])
      else :
        row[rownum] = 0

      if subject.strip() == row[2].strip():
        grade[rowctr] = row[rownum]
      rowctr += 1

  # get unique values in discipline
  once = []
  for occur in discipline:
    if occur not in once:
      once.append(occur)


  for x in range(1, len(once)):
    str = once[x]
    indices = [i for i, y in enumerate(discipline) if y == once[x]]
    sample[str] = indices
    #data.append(indices)   #index of each discipline groupeds

  total_passer = {}
  for a in once:
    gradesum = 0

    if a.upper() != "SUC":
      for grd in sample[a]:
        if grd in grade:
          if a in total_passer:
            gradesum = total_passer[a]
          else:
            gradesum = 0
        
          gradesum += grade[grd]
      
        total_passer[a] = gradesum

  #print total_passer
  associations = total_passer.items();
  associations = sorted(associations, key=lambda pair: pair[1], reverse=True)
  #print associations
  print "8. Top 3  SUC with highest passing rate in " +subject+ " for school year " + school_year 
  print "  1. " + associations[0][0]
  print "  2. " + associations[1][0]
  print "  3. " + associations[2][0]



def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2012')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()