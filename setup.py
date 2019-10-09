from setuptools import setup, find_packages

VERSION = '1.0'

setup(
    name='UltimateSecurityCam',
    version=VERSION,
    description='An easy-to-build, un-hack-able security camera which is impossible to fool.',
    url='https://github.com/NIteshx2/UltimateSecurityCam',
    author='Nitesh Chaudhry',
    author_email='Niteshx22@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['numpy', 'opencv-python', 'pygame'],
    include_package_data=True,
    zip_safe=False
)
