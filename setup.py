from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dsrnet_detector",
    version="0.1.0",
    author="黃毓峰",
    author_email="a288235403@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cvat",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "dominate==2.9.1",
        "einops==0.7.0",
        "kornia==0.7.1",
        "opencv-python==4.9.0.80",
        "PyYAML==6.0.1",
        "scikit-image==0.22.0",
        "scipy==1.12.0",
        "tensorboardX==2.6.2.2",
        "torch",
        "torchvision",
        "visdom==0.2.4",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
        ],
    },
)