from setuptools import setup, find_packages

setup(
    name='Template-Repository',
    version='0.4.0',
    author='Firstpick',
    author_email='kortharshadowbreath@gmail.com',
    description='Template for all my Repositorys',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/firstpick/Template-Repository', # puplic
    packages=find_packages(),
    install_requires=[
        "altgraph==0.17.4"
        "cx_Freeze==7.2.3"
        "cx_Logging==3.2.0"
        "lief==0.15.1"
        "packaging==24.1"
        "pefile==2024.8.26"
        "pyinstaller==6.10.0"
        "pyinstaller-hooks-contrib==2024.8"
        "python-dotenv==1.0.1"
        "pywin32-ctypes==0.2.3"
        "setuptools==75.1.0"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU License',
        'Operating System :: Windows 11',
    ],
    python_requires='>=3.9',
)
