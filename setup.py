import sys, io
from setuptools import setup, find_packages

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

__version__ = "1.0"

def get_requirements():
    with open("requirements.txt") as fp:
        return [req for req in (line.strip() for line in fp) if req and not req.startswith("#")]

ext_modules = [
    Pybind11Extension("rambench",
        ["rambenchmark/rambench.cpp"],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        extra_compile_args=["-O3", "-std=c++11", "-fopenmp", "-shared", "-fPIC"],
        extra_link_args=['-lgomp', "-shared"]
        ),
]

setup(
    name="rambenchmark",
    version=__version__,
    author="Robert Susik",
    author_email="robert.susik@gmail.com",
    url="https://github.com/rsusik/rambenchmark",
        description=(
        "Screen annotation software which allows drawing directly on the screen."
    ),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    entry_points={
        "console_scripts": [
            "rambenchmark=rambenchmark:main",
        ],
    },
    package_dir={"": "."},
    packages = find_packages("."),
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers ",
        "Intended Audience :: Science/Research",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: C++",
        "Topic :: System :: Benchmark",
        "Topic :: System :: Hardware",
        "Operating System :: POSIX :: Linux"
    ],
)
