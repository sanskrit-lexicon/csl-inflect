""" prephelp.py
    converts lgmodel_input.txt to an html table.
"""
import re
f = open("lgmodel_input.txt","r")
lines=f.readlines()
f.close()
f = open("lgmodel_input.html","w")
f.write("<table>\n")
f.write("<tr><th>abbr</th><th>description</th><th>reference</th></tr>\n")
for line in lines:
 (model,descr,kale)=re.split(r'\t',line)
 out = "<tr><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (model,descr,kale)
 f.write(out)
f.write("</table>\n")

f.close()
