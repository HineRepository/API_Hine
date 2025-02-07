from setuptools import setup, find_packages

setup(
    name='Api_Hine',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'sqlalchemy',
        'DatabaseMapping',
        'os',
        'Config',
        'flask_sqlalchemy' 
    ],
    entry_points={
        'console_scripts': [
            'StartApi=Main',
        ],
    },
    author='FT',
    author_email='tuo_email@example.com',
    description='Una breve descrizione del tuo pacchetto',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tuo_username/tuo_repository',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)