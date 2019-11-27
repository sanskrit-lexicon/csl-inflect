# csl-inflect

## continue MWinflect
The csl-inflect repository continues work from MWinflect repository.


## overview
Generate declensions and conjugations based upon words in MW1899 dictionary,
and provide displays.

The generation is done by python programs. In general terms, the process is:
* use Cologne MW digitization to derive stem-model pairs.
* For a given stem,model:
  * if the model is 'ind' (indeclineable) no inflection required. Just gather.
  * if the model is one of several nominal (noun, adjective) models, derive
    a declension table for the stem,model. The stem is MW headword.
  * if the model is one of several verbal models, derive a conjugation
    table for the stem,model.  The stem is MW headword.

When done, the results will be used to improve the underlying data of the
  [inflected forms display](http://www.sanskrit-lexicon.uni-koeln.de/work/fflexphp/web/index.php) of the Cologne Sanskrit-Lexicon web site.



## Reconstruction
The `redo.sh` script recreates all computed files.
Normally, the computed files begin with the 'calc_' prefix, and are not
tracked by Git.

Many recreation steps use 'python3' , which should invoke a Python3 version,
probably a version later than Python3.4.


