import importlib.metadata

packages = ["pandas", "numpy", "matplotlib", "scikit-learn", "flask","util"]

for package in packages:
    try:
        version = importlib.metadata.version(package)
        print(f"{package}: {version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{package}: Not installed")
