"""distrib.py
  Get distribution of 'models' for the inflected verb forms
  python distrib.py temp_input.txt 
"""
import sys,re,codecs

def all_models(d):
 outarr = []
 models = sorted(d.keys())
 nmodels = len(models)
 outarr.append('-------------------------------------------')
 outarr.append('All models (%s)' %nmodels)
 outarr.append('-------------------------------------------')
 for model in models:
  out = '%05d %s' %(d[model],model)
  outarr.append(out)
 n = sum(d[model] for model in models)
 outarr.append('%d inflected forms'%n)
 return outarr

def aggregated_models(d):
 outarr = []
 models = sorted(d.keys())
 d1 = {}
 for model in models:
  dmodel = d[model]
  m = re.search(r'^(.*?)-(.*?)$',model)
  tense,model1 = (m.group(1),m.group(2))
  m = re.search(r'^([0-9]+)([am])$',model1)
  if m:
   c,v = (m.group(1),m.group(2))
   if c in ['1','4','6','10']:
    name = 'spcltense-a-am'
   else:
    name = 'spcltense-b-am'
  elif (tense in ['pre','ipf','ipv','opt']):
   assert model1=='p','Expected passive:%s'%model
   name = 'spcltense-passive'
  else:
   name = tense
  if name not in d1:
   d1[name] = 0
  d1[name] = d1[name]+ dmodel
 #  
 models1 = sorted(d1.keys())
 nmodels1 = len(models1)
 outarr.append('-------------------------------------------')
 outarr.append('Aggretated models (%s)' %nmodels1)
 outarr.append('-------------------------------------------')
 for model in models1:
  out = '%05d %s' %(d1[model],model)
  outarr.append(out)
 n = sum(d1[model] for model in models1)
 outarr.append('%d inflected forms'%n)
 return outarr

if __name__ == "__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2]
 d = {} # dictionary of models, with counts
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   line = line.strip()
   form,model,base = line.split('\t')
   if model not in d:
    d[model] = 0
   d[model] = d[model] + 1
 outarr1 = all_models(d)
 outarr2 = aggregated_models(d)
 outarr = outarr1 + outarr2
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 #print(len(models),"records written to",fileout)

