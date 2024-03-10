# Function to move the mesh
def move_mesh(mesh, x, y, z):
    # Add the displacement to each coordinate
    return [[point[0] + x, point[1] + y, point[2] + z] for point in mesh]