from setuptools import setup, find_packages

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name='matt_pypub',
    version='2.0.7',
    license='MIT',
    author='Andrew Scott',
    author_email='imgurbot12@gmail.com',
    url='https://github.com/imgurbot12/pypub',
    description="A python3 library to generate custom epub books.",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=[
        'jinja2>=3.1.2',
        'pillow>=10.0.0',
        'filetype>=1.2.0'
    ],
    package_data={
        'pypub': [
            'templates/*',
            'static/*',
            'static/css/*',
            'static/img/*',
            'static/fonts/*'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
