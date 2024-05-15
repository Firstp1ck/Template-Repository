from setuptools import setup, find_packages

setup(
    name='Template-Repo',
    version='0.3.2',
    author='Firstpick',
    author_email='kortharshadowbreath@gmail.com',
    description='Template for all my Repositorys',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/firstpick/Template-Repo', # private
    packages=find_packages(),
    install_requires=[
        'altgraph==0.17.4',
        'packaging==24.0',
        'pefile==2023.2.7',
        'pyinstaller==6.6.0',
        'pyinstaller-hooks-contrib==2024.6',
        'python-dotenv==1.0.1',
        'pywin32-ctypes==0.2.2',
        'setuptools==69.5.1'
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
