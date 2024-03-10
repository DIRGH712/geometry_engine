# Getting Started
Before importing this project to your Python workspace, it is necessary to make sure the prerequisite steps are properly done in your development environment.

### Step 1: Clone the GitHub Repository
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Use the command git clone <repository-url>. Replace <repository-url> with the URL of this GitHub repo.
4. Navigate into the cloned repository directory with cd <repository-name>.

### Step 2: Create a `.env` File for Environment Variables
1. Within the root of your cloned repository, create a file named .env.
2. Open the .env file in a text editor and add the following line: JWT_SECRET_KEY=your_jwt_secret_key_here. Replace your_jwt_secret_key_here with a strong, unique secret key.
3. Save and close the .env file.
4. If you provide a .env.example file as a template, make sure it contains JWT_SECRET_KEY=change_this_to_a_secure_key.

### Step 3: Install Dependencies
1. Ensure you are in the root directory of the cloned repository.
2. Run `pip install -r requirements.txt` to install all the necessary packages listed in the requirements.txt file.

### Step 4: Running the Application
1. Set the FLASK_APP environment variable to your application entry file, for example, export FLASK_APP=app.py on macOS/Linux or set FLASK_APP=app.py on Windows, where app.py is the file that initializes your Flask application.
2. Run the application with flask run. This command will start the Flask development server and make your application accessible at http://127.0.0.1:5000/ by default.

# Project Components
- The routes used in this application can be found at `./modules/` which computes appropriate responses for requests made
- A simple index.html page of _('/')_ route can be found in `./template/`
- A suite of unit tests has been provided to ensure that the geometry engine operates correctly
- `utils.py` has precision control code. This showcases the usage of DRY principles.
- The file `requirements.txt` contains all the plugins used for the current application and the app.py file will be responsible for the application execution.


```
Project
├── geometry_engine
│   ├── modules
│   │   ├── bounding_box.py
│   │   ├── check_convexity.py
│   │   ├── get_centroid.py
│   │   ├── move_mesh.py
│   │   ├── optimized_bounding_box.py
│   │   └── rotate_mesh.py
│   └── templates
│       └── index.html
├── tests
│   ├── test_bounding_box.py
│   ├── test_centroid.py
│   ├── test_convexity.py
│   ├── test_move_mesh.py
│   └── test_rotate_mesh.py
├── utils
├── app.py
└── README.md

```

# Running the Test Cases
Follow these steps to run the test cases on your local machine:
- Python’s `unittest` framework provides a feature for automatic discovery of test cases. To use this feature and run all tests, navigate to the root directory of the project where the tests directory is located.
- **Execute:**
   ```bash
    python -m unittest discover -s tests
- If you wish to run a specific test file, use the following command, replacing <test_file>.py with the name of the test file:
   ```bash
    python -m unittest tests/<test_file>.py
   
# Endpoints
**NOTE:** Postman can also be used for testing the following API's <br> 
**NOTE:** Change _http://127.0.0.1:5000_ based on your Flask app. Also copy and paste your URL, to view simple index.html <be>

### 0. Login
- **Endpoint:** `/login`
- **Method:** POST
- **Description:** Returns a valid Access Token which can be used to authenticate every user request with an expiration limit of 30 mins. (Used JWT, and have handled all cases: Invalid, Empty, Expired Token)
- **Input:** JSON with username, password represented as `{"username": "root", "password": "root"}`.
- **Output:** Access Token `{"access_token": "your_access_token"}`.
- **Usage Example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/login \
   -H "Content-Type: application/json" \
   -d '{
     "username": "root",
     "password": "root"
   }'

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
  -H "Authorization: Bearer <Your_Token_Here>" \
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
  -H "Authorization: Bearer <Your_Token_Here>" \
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
  -H "Authorization: Bearer <Your_Token_Here>" \
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
  -H "Authorization: Bearer <Your_Token_Here>" \
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
  -H "Authorization: Bearer <Your_Token_Here>" \
  -d '{
    "vertices": [[0.111, 0.222, 0.333], [2.444, 0.555, 0.666], [0.777, 2.888, 0.999], [0.101, 0.202, 0.303]],
    "precision": 2
  }'


# Implementation Choices and additional notes

## For Computing the smallest Bounding Box
In developing the geometric calculation endpoint, I initiated with the `compute_bounding_box` method, focusing on delivering a robust and straightforward solution for calculating the Axis-Aligned Bounding Box (AABB) for a given set of 3D points. This choice was made by several considerations, emphasizing the importance of efficiency, simplicity, and reliability in software engineering practices.

**Initial Choice Rationale:**

1. **Efficiency & Performance:** The AABB approach, by its nature, offers computational efficiency. It requires minimal processing - essentially, calculating the minimum and maximum values along each axis. This ensures that the endpoint can handle large datasets and perform calculations swiftly, a vital feature for scalable systems.

2. **Simplicity & Maintainability:** Adopting the AABB method allowed me to implement a straightforward and easily understandable algorithm. This simplicity not only accelerates development but also enhances maintainability. It’s a strategy that ensures future developers, or even future me, can quickly grasp and iterate on the existing codebase without a steep learning curve.

3. **Broad Applicability:** Given the wide usage of AABB in various domains, such as computer graphics and collision detection, starting with a universally accepted and straightforward approach ensures the endpoint has a broad range of applicability right out of the gate.

However, recognizing the potential for optimization, a common approach involves computing the convex hull of the set of points and then finding the minimum bounding box of this convex hull. Checkout `optimized_bounding_box.py` in `modules` directory.

**Implementation:**

- Compute the Convex Hull, I learned QuickHull and Gift wrapping algo.
- To find the smallest bounding box, you can use the concept of an oriented bounding box (OBB). An OBB is not axis-aligned, meaning it can have any orientation in space. The OBB that has the minimum volume and contains the convex hull is the solution.
- Perform PCA(Principal Component Analysis) on the set of points to find the principal axes. This can help us get more optimized bounding box.
- Align the points with these axes.
- Compute the bounding box in this aligned configuration for a rough (not necessarily minimal) estimate.
- For the minimal volume box, iterate over all possible orientations (this requires discretizing the rotation space and is computationally expensive), compute the axis-aligned bounding box for the points in each orientation, and find the one with the smallest volume.

# References:

Feel free to review some resources I used to make this project.

- [Convex Hull | Basics | Lecture-1](https://www.youtube.com/watch?v=HojzdCICjmQ)
- [Arbitrarily Oriented Minimum Bounding Box - A Demo ](https://www.youtube.com/watch?v=Ze6lppsly2U)
- [Wiki: Minimum_bounding Box](https://en.wikipedia.org/wiki/Minimum_bounding_box)
- [Book: Computational-Geometry-Algorithms-and-Applications-3rd-Ed](https://erickimphotography.com/blog/wp-content/uploads/2018/09/Computational-Geometry-Algorithms-and-Applications-3rd-Ed.pdf)
- [Some random post](https://discourse.mcneel.com/t/minimum-oriented-bounding-box-implementation-in-grasshopper-python-script-node/64344)
- Khan Academy
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [StackOverflow](https://stackoverflow.com/questions/471962/how-do-i-efficiently-determine-if-a-polygon-is-convex-non-convex-or-complex/472001#472001)






