import subprocess
import sys

def test():
    """Run pytest"""
    sys.exit(subprocess.call(["pytest"] + sys.argv[1:]))

def coverage():
    """Run tests with coverage"""
    # Run tests with coverage using sys.executable to ensure we use the right Python/coverage
    result = subprocess.run([sys.executable, "-m", "coverage", "run", "-m", "pytest"])
    
    if result.returncode == 0:
        # Generate coverage report
        subprocess.run([sys.executable, "-m", "coverage", "report"])
    
    sys.exit(result.returncode)