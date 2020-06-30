import setuptools

setuptools.setup(
    name='django-manage',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/manage.py']
)
