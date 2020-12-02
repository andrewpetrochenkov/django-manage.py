import setuptools

setuptools.setup(
    name='django-manage',
    version='2020.12.2',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/manage.py']
)
