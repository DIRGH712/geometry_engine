# Endpoints
NOTE: Change _http://127.0.0.1:5000_ based on your Flask app <br>
### 1. Compute Bounding Box
- **Endpoint:** `/compute-bounding-box`
- **Method:** POST
- **Description:** Calculates the smallest axis-aligned bounding box that contains all the given 3D points.
- **Input:** JSON with an array of points, where each point is represented as `{"points": [[x1, y1, z1], [x2, y2, z2] ...]}`.
- **Output:** JSON with the minimum and maximum points of the bounding box, formatted as `{"min_point": [x1, y1, z1], "max_point": [x2, y2, z2]}`.
- **Usage Example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/compute-bounding-box \
  -H "Content-Type: application/json" \
  -d '{
    "points": [[0, 0, 0], [1, 1, 1]]
  }'

### 2. Rotate Mesh
- **Endpoint:** `/rotate-mesh`
- **Method:** POST
- **Description:** Rotates a 3D mesh by a specified angle around the given axis.
- **Input:** JSON with the 3D mesh data, rotation angle, axis, and optional precision: `{"mesh": [[x1, y1, z1], ...], "angle": float, "axis": "X"|"Y"|"Z", "precision": int}`.
- **Output:** JSON with the rotated 3D mesh data.
- **Usage Example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/rotate-mesh \
  -H "Content-Type: application/json" \
  -d '{
    "mesh": [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]],
    "angle": 30,
    "axis": "Y",
    "precision": 2
  }'

### 3. Move Mesh
- **Endpoint:** `/move-mesh`
- **Method:** POST
- **Description:** Moves a 3D mesh by specified amounts along the X, Y, and Z axes.
- **Input:** JSON with the mesh data and translation values: `{"mesh": [[x1, y1, z1], [x2, y2, z2]...], "x": float, "y": float, "z": float}`.
- **Output:** JSON with the moved mesh data.
- **Usage Example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/move-mesh \
  -H "Content-Type: application/json" \
  -d '{
    "mesh": [[0, 0, 0], [1, 1, 1], [2, 2, 2]],
    "x": 10,
    "y": 20,
    "z": 30
  }'

### 4. Check Convexity
- **Endpoint:** `/check-convexity`
- **Method:** POST
- **Description:** Check whether a given polygon in 3D space is convex.
- **Input:** JSON with an array of 3D points representing the polygon vertices: `{"points": [[x1, y1, z1], [x2, y2, z2],...]}`.
- **Output:** JSON with the appropriate message, whether it's a polygon or not, or if the convexity cannot be checked: `{"message": message}`.
- **Usage Example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/check-convexity \
  -H "Content-Type: application/json" \
  -d '{
    "points": [[0, 0, 0], [2, 0, 0], [2, 2, 0], [0, 2, 0]]
    }'

### 5. Calculate Centroid [Bonus]
- **Endpoint:** `/calculate-centroid`
- **Method:** POST
- **Description:** Calculates the centroid of a set of vertices.
- **Input:** JSON with an array of vertices and optional precision: `{"vertices": [[x1, y1, z1], [x2, y2, z2]...], "precision": int}`.
- **Output:** JSON with the centroid data.
- **Usage Example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/calculate-centroid \
  -H "Content-Type: application/json" \
  -d '{
    "vertices": [[0.111, 0.222, 0.333], [2.444, 0.555, 0.666], [0.777, 2.888, 0.999], [0.101, 0.202, 0.303]],
    "precision": 2
  }'
