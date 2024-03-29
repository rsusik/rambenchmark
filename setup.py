import sys, io, platform
from setuptools import setup, find_packages, Extension

__version__ = "1.3"

def get_requirements():
    with open("requirements.txt") as fp:
        return [req for req in (line.strip() for line in fp) if req and not req.startswith("#")]


if sys.version_info >= (3,) and platform.python_implementation() == 'CPython':
    try:
        import wheel.bdist_wheel
    except ImportError:
        cmdclass = {}
    else:
        class bdist_wheel(wheel.bdist_wheel.bdist_wheel):
            def finalize_options(self):
                self.py_limited_api = 'cp3{}'.format(sys.version_info[1])
                return super().finalize_options()
        cmdclass = {'bdist_wheel': bdist_wheel}

ext_modules = [
    Extension("rambench",
        ["rambenchmark/_rambench.cpp", "rambenchmark/rambench.cpp"],
        define_macros = [
            ('VERSION_INFO', __version__),
            ('Py_LIMITED_API', None)
        ],
        py_limited_api=True,
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
        "RAM memory benchmark."
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
    cmdclass=cmdclass,
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
