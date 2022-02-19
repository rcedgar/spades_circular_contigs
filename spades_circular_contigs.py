#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    sys.stderr.write("\n\nIdentify and trim circular contigs from SPAdes with given k-mer length.\n\n")
    sys.stderr.write("\nUsage example:\n")
    sys.stderr.write("  python3 spades_circular_contigs.py 73 contigs.fa > circular_contigs.fa\n\n")
    sys.exit(1)

ContigsFileName = sys.argv[1]
k = int(sys.argv[2])

def WriteSeq(Label, Seq):
	sys.stdout.write(">" + Label + "\n")
	W = 80
	SeqLength = len(Seq)
	BlockCount = int((SeqLength + (W-1))/W)
	for BlockIndex in range(0, BlockCount):
		Block = Seq[BlockIndex*W:]
		Block = Block[:W]
		sys.stdout.write(Block + "\n")

def OnSeq(Label, Seq):
    global N, C
    N += 1
    if len(Seq) < 2*k:
        return
    First = Seq[0:k]
    Last = Seq[-k:]
    if First == Last:
        TrimmedSeq = Seq[:-k]
        assert len(TrimmedSeq) == len(Seq) - k
        C += 1
        WriteSeq(Label, TrimmedSeq)

Label = None
Seq = ""
N = 0
C = 0
File = open(ContigsFileName)
while 1:
    Line = File.readline()
    if len(Line) == 0:
        if Seq != "":
            OnSeq(Label, Seq)
        break
    Line = Line.strip()
    if len(Line) == 0:
        continue
    if Line[0] == ">":
        if Seq != "":
            OnSeq(Label, Seq)
        Label = Line[1:]
        Seq = ""
    else:
        Seq += Line.replace(" ", "")

sys.stderr.write("%d / %d circular contigs found\n" % (C, N))
