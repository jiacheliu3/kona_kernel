from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='k_kernel',
    version='1.1',
    packages=['k_kernel'],
    description='Simple example kernel for Jupyter',
    long_description=readme,
    author='Jiacheng Liu',
    author_email='jiacheliu3@gmail.com',
    url='https://github.com/jiacheliu3/k_kernel',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
