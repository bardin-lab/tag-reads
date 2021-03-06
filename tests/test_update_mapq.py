from collections import namedtuple
from readtagger.bam_io import BamAlignmentReader as Reader
from readtagger.cli.update_mapq import update_mapq
from .helpers import namedtuple_to_argv

SOURCE_BAM = 'supplementary.bam'
REMAPPED_BAM = 'remapped_supplementary.bam'
TEMPLATE_ARGS = namedtuple('args', ['source_path', 'remapped_path', 'output_path'])


def test_update_mapq(datadir_copy, tmpdir, mocker):  # noqa: D103
    out = tmpdir.join('out.bam').strpath
    args = TEMPLATE_ARGS(source_path=str(datadir_copy[SOURCE_BAM]), remapped_path=str(datadir_copy[REMAPPED_BAM]), output_path=out)
    argv = namedtuple_to_argv(args, 'update_mapq.py')
    mocker.patch('sys.argv', argv)
    mocker.patch('sys.exit')
    update_mapq()
    with Reader(out) as reader:
        assert len([r for r in reader if r.mapq == 0]) == 0
