from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    description="A simple math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mfaizanlive/dsss_homework_2",
    author="Faizan Iqbal",
    author_email="mfaizanlive@hotmail.com",
    license="Apache License 2.0",
    install_requires=[],
    entry_points={
    'console_scripts': [
        'math_quiz = math_quiz.math_quiz:math_quiz',
    ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
