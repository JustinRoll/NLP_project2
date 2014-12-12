Our code has the following dependencies:
Python 3.4
NLTK 3
Scikit-Learn (via Anaconda) http://repo.continuum.io/anaconda3/Anaconda3-2.1.0-Windows-x86_64.exe
ConceptNet 5 Client https://github.com/israkir/conceptnet5-client/archive/master.zip

The main class of the project is detectDriver.py. To run for the AN phrases, use the argument anPairs and the optional
parameter met_type="an".  To use the SVO phrases, use the argument svoPairs and the optional parameter
met_type="svo".  To run against the aggregate of the judges, do not provide the optional judges parameter.
To run againsta a specific judge, use the optional parameter judge=<number 0-4>.

To change which features are used, edit the file feature extractor.py.  Comment out features you
do not wish to use for your test.  Note that there are separate functions for SVO and AN feature extraction.

All data files should be placed under the data directory.