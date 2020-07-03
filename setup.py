from setuptools import setup 

# setting up the cli
setup(
    name = 'python_cli',
    version = "0.1.0",
    packages = ['zindi'],
    entry_points = {
        'console_scripts':[
            'zindi = zindi.__main__:main'
        ]
    }

)