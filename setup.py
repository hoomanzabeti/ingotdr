from setuptools import setup

setup(
    name='ingotdr',
    version='0.0.1',
    description="INGOT-DR (INterpretable GrOup Testing for Drug Resistance)",
    author="Hooman Zabeti",
    author_email="hzabeti@sfu.ca",
    url="https://github.com/hoomanzabeti/ingotdr",
    py_modules=["INGOT"],
    package_dir={'': 'src'}
)
