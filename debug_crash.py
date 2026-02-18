import sys
import os

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    import pkg_resources
    print("SUCCESS: pkg_resources imported.")
except ImportError as e:
    print(f"FAILURE: pkg_resources not found. Error: {e}")

try:
    import face_recognition_models
    print(f"SUCCESS: face_recognition_models imported. File: {face_recognition_models.__file__}")
except ImportError as e:
    print(f"FAILURE: face_recognition_models import failed. Error: {e}")
except Exception as e:
    print(f"FAILURE: face_recognition_models failed with error: {e}")

try:
    import face_recognition
    print("SUCCESS: face_recognition imported.")
except Exception as e:
    print(f"FAILURE: face_recognition import failed. Error: {e}")
