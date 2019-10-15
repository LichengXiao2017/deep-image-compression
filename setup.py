import os
from distutils.core import setup

install_requires = [
    'tensorflow-gpu==1.15.0-rc1',
    'absl-py==0.8.0',
    'opencv-python==4.1.1.26',
    'argparse',
    'glob',
    'tensorflow_compression',
    'numpy',
]

tests_require = [
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx<1.5.0,>=1.4.2',
        'docutils<0.13,>=0.12',
    ],
}

setup_requires = ['pytest-runner>=2.6.2', ]

setup(
    name='deep-image-compression',         # How you named your package folder (MyLib)
    packages=['deep-image-compression'],   # Chose the same as "name"
    version='0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='A tool to build, train and analyze deep learning models for image compression',
    author='Licheng Xiao',                   # Type in your name
    author_email='david.xiao.2008@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/LichengXiao2017/deep-image-compression',
    # I explain this later on
    download_url='https://github.com/LichengXiao2017/deep-image-compression/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['image', 'compression', 'deep learning'],
    install_requires=install_requires,
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
