from setuptools import setup, find_packages

with open("README.md", "r") as f:
    content = f.read()

setup(
    name="gruvboxify",
    version="1.1.0",
    packages=find_packages(),
    install_requires = [
        "numpy>=2.2.2",
        "Pillow>=10.0.0"
    ],
    entry_points = {
        "console_scripts": [
            "gruvboxify = gruvboxify:main",
        ],
    },
    long_description=content,
    long_description_content_type="text/markdown"
)
