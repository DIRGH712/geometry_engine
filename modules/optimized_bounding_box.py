import numpy as np
from scipy.spatial import ConvexHull
from sklearn.decomposition import PCA


def compute_3d_convex_hull(points):
    """Compute the convex hull of a set of 3D points."""
    hull = ConvexHull(points)
    return points[hull.vertices]


def apply_pca(hull_points):
    """Apply PCA to find principal axes of the hull points."""
    pca = PCA(n_components=3)
    pca.fit(hull_points)
    return pca


def align_points_to_principal_axes(hull_points, pca):
    """Rotate hull points to align with principal axes."""
    return pca.transform(hull_points)


def find_bounding_box_extents(aligned_points):
    """Find the minimum and maximum extents of aligned points."""
    min_extent = np.min(aligned_points, axis=0)
    max_extent = np.max(aligned_points, axis=0)
    return min_extent, max_extent


def main():

    points = np.random.rand(100, 3)

    # Compute the convex hull of these points
    hull_points = compute_3d_convex_hull(points)

    # Apply PCA to find principal axes
    pca = apply_pca(hull_points)

    # Align points to these axes
    aligned_points = align_points_to_principal_axes(hull_points, pca)

    # Determine the bounding box extents
    min_extent, max_extent = find_bounding_box_extents(aligned_points)

    # Print results (for demonstration purposes)
    print(f"Minimum Extent: {min_extent}")
    print(f"Maximum Extent: {max_extent}")


if __name__ == "__main__":
    main()
