# spades_circular_contigs
Python script to identify circular contigs from SPAdes assembler and trim the repeated k-mer found at both terminals.

Usage:

<pre>
python3 ./spades_circular_contigs.py contigs.fa 73 > circles.fa
</pre>

Replace 73 with SPAdes k-mer length as needed.
