import sys
import argparse

##### parse arguments
parser = argparse.ArgumentParser(description="Converters a .vcf file to a .bed file.");
parser.add_argument('-i', '--input', required=True, help="The name of the input .vcf file.");
parser.add_argument('-o', '--output', required=False, help="The name of the file to output to (will overwrite file if it already exists). If this argument is not specified, output will be to stdout");

_args = parser.parse_args();
globals()['args'] = _args;
#####

##### ___main___ #####

if args.input[-4:] != ".vcf":
    print("Input file is not a .vcf file");
    sys.exit();

if args.input == args.output:
    print("Input and output cannot be the same file")
    sys.exit()

vcf_file = open(args.input);
if args.output != None:
    bed_stream = open(args.output, "w");
else:
    bed_stream = sys.stdout

for line in vcf_file:
    fields = line.split('\t')

    chrom = fields[0]
    pos = int(fields[1])
    idd = fields[2]
    ref = fields[3]

    bed_stream.write('\t'.join(["chr" + chrom, str(pos - 1), str(pos + (len(ref) - 1))]));
    for i in range(2, len(fields)):
        bed_stream.write("\t" + fields[i])


#########################
