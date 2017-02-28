from readtagger.findcluster import ClusterFinder

INPUT = 'tagged_dm6.bam'
EXTENDED = 'extended_and_annotated_roi.bam'


def test_clusterfinder_single_cluster(datadir):  # noqa: D103
    input_path = datadir[INPUT]
    cf = ClusterFinder(input_path=input_path)
    assert len(cf.cluster) == 1
    assert len(cf.cluster[0]) == 27


def test_clusterfinder_multiple_cluster(datadir, tmpdir):  # noqa: D103
    input_path = datadir[EXTENDED]
    output_path = tmpdir.join('tagged_clusters.bam')
    cf = ClusterFinder(input_path=input_path, output_path=output_path.strpath)
    assert len(cf.cluster) == 3
