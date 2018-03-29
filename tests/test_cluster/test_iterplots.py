# tests.test_cluster.test_silhouette
# Tests for the SilhouetteVisualizer
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Mon Mar 27 10:01:37 2017 -0400
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: test_silhouette.py [57b563b] benjamin@bengfort.com $

"""
Tests for the SilhouetteVisualizer
"""

##########################################################################
## Imports
##########################################################################
import numpy as np

from ..base import VisualTestCase

from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.datasets import make_blobs

from yellowbrick.exceptions import YellowbrickValueError
from yellowbrick.cluster.iterplots import IterLabelsVisualizer


##########################################################################
## SilhouetteVisualizer Test Cases
##########################################################################

class IterLabelsVisualizerTests(VisualTestCase):

    def test_integrated_kmeans_silhouette(self):
        """
        Test no exceptions for kmeans silhouette visualizer on blobs dataset

        See #182: cannot use occupancy dataset because of memory usage
        """

        # Generate a blobs data set
        X, _ = make_blobs(
            n_samples=1000, n_features=12, centers=8, shuffle=False, random_state=0
        )
        y = np.random.randint(5, size=X.shape[0])

        visualizer = IterLabelsVisualizer(KMeans)
        visualizer.fit(X, y)
        visualizer.poof()

    def test_integrated_mini_batch_kmeans_silhouette(self):
        """
        Test no exceptions for mini-batch kmeans silhouette visualizer

        See #182: cannot use occupancy dataset because of memory usage
        """

        # Generate a blobs data set
        X, _ = make_blobs(
            n_samples=1000, n_features=12, centers=8, shuffle=False, random_state=0
        )
        y = np.random.randint(5, size=X.shape[0])

        visualizer = IterLabelsVisualizer(MiniBatchKMeans)
        visualizer.fit(X, y)
        visualizer.poof()