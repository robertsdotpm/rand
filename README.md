# compress_research

The following code is part of my research on compressing random data. It's a program designed to run on a pyspark cluster and isn't worth going into until its fully finished and working. But the program demonstrates my overall approach of attempting to reconstruct random data from golomb-coded sets using nonce puzzles. It's my hope that I can finish this work if I get access to more computing resources or interest.

Main program is: test_data.py which shows how data is converted to a GCS set -> node list, edge hashes, then nonce puzzles, with an unfinished algorithm to reconstruct the node lists using the puzzles.

Details available here: http://roberts.pm/random_data_compression