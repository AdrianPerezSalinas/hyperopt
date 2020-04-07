import setuptools

setuptools.setup(
    name="hyperopt",
    version="0.2.3",
    packages=setuptools.find_packages(include=["hyperopt*"]),
    entry_points={"console_scripts": ["hyperopt-mongo-worker=hyperopt.mongoexp:main"]},
    url="http://hyperopt.github.com/hyperopt/",
    author="James Bergstra",
    author_email="james.bergstra@gmail.com",
    description="Distributed Asynchronous Hyperparameter Optimization",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    platforms=["Linux", "OS-X", "Windows"],
    license="BSD",
    keywords="Bayesian optimization hyperparameter model selection",
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "six",
        "networkx>=2.2",
        "future",
        "tqdm",
        "cloudpickle",
    ],
    extras_require={
        "SparkTrials": "pyspark",
        "MongoTrials": "pymongo",
        "ATPE": ["lightgbm", "scikit-learn"],
        "dev": ["black", "pre-commit", "nose", "pytest"],
    },
    tests_require=["nose", "pytest"],
    zip_safe=False,
)
