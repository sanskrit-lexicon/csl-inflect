# -*- coding: utf-8 -*-
""" conj_compare.py
  compare pysanskritv1 and pysanskritv2 
"""
import sys,codecs,re
import conjugate_file_v2 as v2
sys.path.append('../../pysanskritv1/')
import conjugate_file_v1 as v1

def known_diffs_note(line,notes):
 """ Return a string classifying the difference.
     
 """
 rec = v2.ConjRec(line)
 (model,verb) = (rec.model, rec.verb)
 (c,v,tense) = (rec.theclass,rec.voice,rec.tense)
 key = '%s %s' %(verb,model)
 if key in notes:
  note = notes[key]
 else:
  note = 'unknown'
 return note

def init_notes(filein):
 notes = {}
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   line = line.rstrip('\r\n')
   if line.startswith(';'):
    continue # comment
   m = re.search(r'^(.*?) +(.*?) +(.*)$',line)
   if not m:
    print('conj_compare_notes: init_notes error')
    print(line)
    continue
   verb,model,note = (m.group(1),m.group(2),m.group(3))
   key = verb + ' ' + model
   notes[key] = note
 return notes

def compare(line,notes):
 v2_conj = v2.ConjRec(line)
 v1_conj = v1.ConjRec(line)
 outarr = []
 status = compare_infl(v1_conj.inflection , v2_conj.inflection)
 #status = v1_conj.inflection == v2_conj.inflection
 if status:
  outarr.append('v1 == v2 for %s\t%s' %(line,v1_conj.inflection))
 else:
  note = known_diffs_note(line,notes)
  outarr.append('v1 != v2 for %s (%s)' % (line,note))
  outarr.append('v1: %s' % v1_conj.inflection)
  outarr.append('v2: %s' % v2_conj.inflection)
 return status,outarr

def compare_infl(infl1, infl2):
 if infl1 == infl2:
  return True
 # handle cases with two bases in infl2
 # This is indicated by presence of '&' in infl2
 parts2 = infl2.split('&')
 if len(parts2) == 1:
  return False  # only one base
 # 2 or more bases in 2nd form
 nparts2 = len(parts2)
 ans1 = [[] for i in range(0,nparts2)]
 items1 = infl1.split(':')
 for item in items1:
  subitems = item.split('/')
  if len(subitems) != nparts2:
   return False
  for i in range(0,nparts2):
   ans1[i].append(subitems[i])
 parts1 = [':'.join(ans1[i]) for i in range(0,nparts2)]
 return sorted(parts1) == sorted(parts2)
if __name__ == "__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2]
 filenotes = "conj_compare_notes.txt"
 print('conj_compare_file uses notes from',filenotes)
 notes = init_notes(filenotes)
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
 nprob = 0
 f = codecs.open(fileout,"w","utf-8")
 for line in lines:
  (status,outarr) = compare(line,notes)
  if not status:
   nprob = nprob + 1
  for out in outarr:
   f.write(out + '\n')
 f.close()
 print(nprob,'differences out of',len(lines),'examples')


 
