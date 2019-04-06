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
    firstTabIndex = line.index('\t');
    secondTabIndex = line.index('\t', firstTabIndex + 1);
    thirdTabIndex = line.index('\t', secondTabIndex + 1);
    fourthTabIndex = line.index('\t', thirdTabIndex + 1);
    ref = line[thirdTabIndex:fourthTabIndex]
    pos = int(line[firstTabIndex:secondTabIndex]);
    bed_stream.write('\t'.join(["chr" + line[0:firstTabIndex], str(pos - 1), str(pos), line[secondTabIndex + 1:]]));

#########################
