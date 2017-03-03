from collections import namedtuple
from readtagger.findcluster import ClusterFinder
from readtagger.cli import findcluster

from .helpers import namedtuple_to_argv

INPUT = 'tagged_dm6.bam'
CORNERCASE = 'cornercase.bam'
EXTENDED = 'extended_and_annotated_roi.bam'


def test_clusterfinder_single_cluster(datadir):  # noqa: D103
    input_path = datadir[INPUT]
    cf = ClusterFinder(input_path=input_path)
    assert len(cf.cluster) == 1
    assert len(cf.cluster[0]) == 27


def test_cornercase(datadir, tmpdir):  # noqa: D103
    input_path = datadir[CORNERCASE]
    output_gff = tmpdir.join('output.gff').strpath
    cf = ClusterFinder(input_path=input_path, output_gff=output_gff)
    assert len(cf.cluster) == 1


def test_clusterfinder_multiple_cluster(datadir, tmpdir):  # noqa: D103
    input_path = datadir[EXTENDED]
    output_bam = tmpdir.join('tagged_clusters.bam')
    cf = ClusterFinder(input_path=input_path, output_bam=output_bam.strpath)
    assert len(cf.cluster) == 3


def test_clusterfinder_multiple_cluster_gff(datadir, tmpdir):  # noqa: D103
    input_path = datadir[EXTENDED]
    output_gff = tmpdir.join('output.gff')
    cf = ClusterFinder(input_path=input_path, output_gff=output_gff.strpath)
    assert len(cf.cluster) == 3


def test_clusterfinder_cache(datadir, tmpdir, mocker):  # noqa: D103
    input_path = datadir[EXTENDED]
    output_gff = tmpdir.join('output.gff')
    cf = ClusterFinder(input_path=input_path, output_gff=output_gff.strpath)
    assert len(cf.cluster) == 3
    mocker.spy(cf.cluster[0], 'can_join')
    mocker.spy(cf.cluster[0], '_can_join')
    cf.join_clusters()
    assert cf.cluster[0].can_join.call_count == 2
    assert cf.cluster[0]._can_join.call_count == 0


def test_clusterfinder_multiple_cluster_gff_cli(datadir, tmpdir, mocker):  # noqa: D103
    input_path = datadir[EXTENDED]
    output_bam = tmpdir.join('output.bam').strpath
    output_gff = tmpdir.join('output.gff').strpath
    args_template = namedtuple('ArgumentParser', 'input_path output_gff output_bam')
    args = args_template(input_path=input_path, output_bam=output_bam, output_gff=output_gff)
    argv = namedtuple_to_argv(args)
    mocker.patch('sys.argv', argv)
    findcluster.main()
