import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pomodoro-timer",
    version="0.1",
    author="Evgeniy Asvatov",
    author_email="evgeniy.asvatov@phystech.edu",
    description="A pomodoro timer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT License',
    keywords='pomodoro-timer pomodoro timer indicator time-management',
    url="https://github.com/asvatov/pomodoro-timer",
    project_urls={
        'Documentation': 'https://github.com/asvatov/pomodoro-timer',
        'Funding': 'https://www.patreon.com/hippiest',
        'Say Thanks!': 'https://saythanks.io/to/asvatov',
        'Source': 'https://github.com/asvatov/pomodoro-timer',
        'Tracker': 'https://github.com/asvatov/pomodoro-timer/issues',
    },
    # py_modules=["six"],
    install_requires=["pydub"],
    python_requires='>=3',
    # package_data={},
    # data_files=[('my_data', ['data/data_file'])],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pomodoro-timer=pomodoro_timer.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
    ]
)
