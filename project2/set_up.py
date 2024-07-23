from setuptools import setup, find_packages

setup(
    name='my_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        
    ],
    author='Krutoy',
    author_email='',
    description='Описание вашей библиотеки',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ваш_репозиторий',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)