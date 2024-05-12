from setuptools import setup, find_packages

setup(
    name='Template-Repo',
    version='0.1.0',
    author='Firstpick',
    author_email='kortharshadowbreath@gmail.com',
    description='Template for all my Repos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/firstpick/Template-Repo',
    packages=find_packages(where='src'),  # where your Python packages are
    package_dir={'': 'src'},
    install_requires=[
        'Example_Lib',  # List your project's dependencies here. They will be installed automatically when using pip to install your package
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU License',
        'Operating System :: Windows 11',
    ],
    python_requires='>=3.7',
)
