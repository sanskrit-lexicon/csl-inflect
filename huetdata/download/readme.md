## Huet Data download

This directory contains data 
inflection data published by [Gerard Huet](https://sanskrit.inria.fr/).

The data itself is not part of this repository.  
In order to make use of the extraction programs of this repository, 
a user needs to download his own copy of Huet's data, and name the
resulting as described in the next comment.

## To Download and Decompress, with curl

```
# First, cd into this directory. Then
curl https://sanskrit.inria.fr/DATA/XML/SL_morph_dtd.txt -o SL_morph.dtd
curl https://sanskrit.inria.fr/DATA/XML/SL_morph.xml.gz -o SL_morph.xml.gz
gunzip SL_morph.xml.gz
# (result is SL_morph.xml)
#Note: gunzip removes SL_morph.xml.gz
```



