import argparse
from readtagger import findcluster
from readtagger.readtagger import __VERSION__


def parse_findcluster_args():
    """Parse commandline arguments for findcluster script."""
    p = argparse.ArgumentParser(description="Find clusters of reads that support a TE insertion.",
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--input_path', help='Find cluster in this BAM file.', required=True)
    p.add_argument('--output_bam', help='Write out BAM file with cluster information to this path. '
                                        'Reads will have an additional "CD" tag to indicate the cluster number')
    p.add_argument('--output_gff', help='Write out GFF file with cluster information to this path.')
    p.add_argument('--version', action='version', version=__VERSION__)
    args = p.parse_args()
    if not (args.output_bam or args.output_gff):
        args.error('No output path given, need at least an output bam path or an output_gff path.')
    return args


def main(args=None):
    """Parse arguments and launch findcluster."""
    if not args:
        args = parse_findcluster_args()
    findcluster.ClusterFinder(input_path=args.input_path, output_bam=args.output_bam, output_gff=args.output_gff)


if __name__ == '__main__':
    args = parse_findcluster_args()
