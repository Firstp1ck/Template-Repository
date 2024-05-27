from setuptools import setup, find_packages

setup(
    name='Template-Repository',
    version='0.3.8',
    author='Firstpick',
    author_email='kortharshadowbreath@gmail.com',
    description='Template for all my Repositorys',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/firstpick/Template-Repository', # puplic
    packages=find_packages(),
    install_requires=[
        "python-dotenv==1.0.1"
        "setuptools==69.5.1"
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
