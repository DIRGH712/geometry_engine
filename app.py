from flask import Flask, jsonify, request, render_template
from modules.rotate_mesh import rotate_mesh
from modules.move_mesh import move_mesh
from modules.check_convexity import is_convex_polygon
from modules.get_centroid import calculate_centroid
from modules.bounding_box import compute_bounding_box
import os
from datetime import timedelta
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

load_dotenv()  # This will load the environment variables from the .env file

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
jwt = JWTManager(app)


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    # Invalid token, maybe not signed or tampered with
    return jsonify({'error': 'Invalid token.'}), 401


# Callback function to check if a token has expired
@jwt.expired_token_loader
def expired_token_callback(callback):
    # Expired token, return error string with 401 status code
    return jsonify({'error': 'Expired token.'}), 401


# Callback function to check if a token is not present
@jwt.unauthorized_loader
def missing_token_callback(callback):
    # No token, return error string with 401 status code
    return jsonify({'error': 'Authorization header is missing.'}), 401


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != "root" or password != "root":
        return jsonify({"msg": "Bad username or password"}), 401

    # Create JWT access token
    access_token = create_access_token(identity=username, expires_delta=timedelta(minutes=30))
    return jsonify(access_token=access_token)


@app.route('/compute-bounding-box', methods=['POST'])
@jwt_required()
def compute_aabb_endpoint():
    data = request.get_json()
    points = data.get('points')

    if points is None:
        return jsonify({"error": "No points data provided"}), 400

    try:
        min_point, max_point = compute_bounding_box(points)
        return jsonify({
            "min_point": min_point.tolist(),
            "max_point": max_point.tolist()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/rotate-mesh', methods=['POST'])
@jwt_required()
def rotate_mesh_endpoint():
    data = request.get_json()
    mesh = data.get('mesh')
    angle = data.get('angle')
    axis = data.get('axis')
    precision = data.get('precision', 2)

    if not all([mesh, angle, axis]):
        return jsonify({"error": "Missing data for mesh, angle, or axis"}), 400

    try:
        rotated_mesh = rotate_mesh(mesh, angle, axis, precision)
        return jsonify({"rotated_mesh": rotated_mesh})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/move-mesh', methods=['POST'])
@jwt_required()
def move_mesh_endpoint():
    data = request.get_json()
    mesh = data.get('mesh')
    x = data.get('x')
    y = data.get('y')
    z = data.get('z')

    if not mesh or x is None or y is None or z is None:
        return jsonify({"error": "Missing data for mesh or translation values"}), 400

    try:
        moved_mesh = move_mesh(mesh, x, y, z)
        return jsonify({"moved_mesh": moved_mesh})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/check-convexity', methods=['POST'])
@jwt_required()
def check_convexity_endpoint():
    data = request.get_json()
    polygon = data.get('points')

    if not polygon:
        return jsonify({"error": "No polygon data provided"}), 400

    try:
        is_convex = is_convex_polygon(polygon)
        return jsonify({"message": is_convex})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/calculate-centroid', methods=['POST'])
@jwt_required()
def calculate_centroid_endpoint():
    data = request.get_json()
    vertices = data.get('vertices')
    precision = data.get('precision', 2)  # Optional precision parameter

    if not vertices:
        return jsonify({"error": "No vertices data provided"}), 400

    try:
        centroid = calculate_centroid(vertices, precision)
        return jsonify({"centroid": centroid})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
