from setuptools import setup, find_packages

setup(
    name='bloxnickgenerator', 
    version='0.1.0',  
    packages=find_packages(), 
    install_requires=[  
        'requests',
        'Faker',
    ],
    description='A simple username generator for Roblox',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    author='Kayon',
    author_email='kayop621@gmail.com',  
    url='https://github.com/realkayo/Roblox-Nickname-Generator',
    classifiers=[  
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
