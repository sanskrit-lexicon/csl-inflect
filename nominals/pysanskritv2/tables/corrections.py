""" corrections.py
"""
import sys,re,codecs
import tableread

def add_manual_tables(d,filein):
 """ modify d
 """
 recs = tableread.init_table(filein)
 for rec in recs:
  # a Table object
  key = (rec.model,rec.key2)
  # Do not allow possibility of duplicate 'keys'
  #if key in d:
  # print('add_manual_tables WARNING: duplicate key',key,"in file",filein)
  #else:
  # d[key] = rec.table
  
  # Allow possibility of duplicate 'keys'
  if key not in d:
   d[key] = []
  else:
   print('manual duplicate key',key,filein)
  #d[key].append(rec.table)
  d[key] = rec

def init_manual_tables(filein):
 with codecs.open(filein,"r","utf-8") as f:
  filenames = [x.rstrip() for x in f if not x.startswith(';')]
 d = {}
 for filename in filenames:
  add_manual_tables(d,filename)
 return d

def process(line,d,iline):
 """  If line has a correction in d, change and return new line
   otherwise, return line.
   line is assumed to be in format written by decline_file
     '%s\t%s\t%s\t%s' %(rec.model,rec.key2,rec.refs,rec.inflection)
 """
 try:
  model,key2,refs,inflection = line.split('\t')
 except:
  print('process ERROR. wrong format of old line #',iline+1)
  print(line)
  exit(1)
 dkey = (model,key2)  # consistent with add_manual_tables
 if dkey not in d:
  return line
 rec = d[dkey]
 new_inflection = rec.tabstring
 newline = '%s\t%s\t%s\t%s' % (model,key2,refs,new_inflection)
 rec.nused = rec.nused + 1
 print('new inflection for',dkey)
 return newline
if __name__ == "__main__":
 filein = sys.argv[1]   # tables produced by decline_file
 filein1 = sys.argv[2]  # inventory of correction files
 fileout = sys.argv[3]  # output tables, same format as filein

 d = init_manual_tables(filein1)
 with codecs.open(filein,"r","utf-8") as f:
  with codecs.open(fileout,"w","utf-8") as fout:
   for iline,line in enumerate(f):
    line = line.rstrip()
    lineout = process(line,d,iline)
    fout.write(lineout+'\n')
 # check unused tables
 dupkeys = [k for k in d.keys() if d[k].nused == 0]
 print(len(d.keys()),' = # of correction records')
 print(len(dupkeys),'= # of unused corrections')

