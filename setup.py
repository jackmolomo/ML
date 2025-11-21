from setuptools import setup, find_packages

HYPhen_e_dot = '-e .'

def get_requirements(file_path: str) -> list[str]:
    """
    Read a requirements.txt file and return a list of dependencies.

    Args:
        file_path (str): Path to the requirements.txt file.

    Returns:
        list[str]: List of package requirements.
    """
    with open(file_path, "r") as f:
        requirements = f.read().splitlines()
    
    # Remove newline characters manually
    requirements = [reg.replace("\n", "") for reg in requirements]

    # Remove empty lines and comments
    requirements = [req for req in requirements if req.strip() and not req.startswith("#")]

    # Remove '-e .' if present
    if HYPhen_e_dot in requirements:
        requirements.remove(HYPhen_e_dot)
    
    return requirements

setup(
    name="MLProject",
    version="0.1.0",
    author="jackmolomo",
    author_email="jackmolomo@gmail.com",
    description="My Machine Learning project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires='>=3.8',
)
