from setuptools import setup , find_packages
HYPEN_E = '-e.'


def get_packages_and_install(filepath):
    requirements = []
    '''This Function is used to install the packages'''
    with open(filepath) as file :
        requirements = file.readlines()
        requirements = [ req.replace('\n', '') for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements


setup(
    name='Rock VS Mine Detection Project',
    version='1.0',
    author='Viraj Gavade',
    author_email='vrajgavade17@gmail.com',
    install_requires= get_packages_and_install('requirements.txt') ,
    packages=find_packages()
)

