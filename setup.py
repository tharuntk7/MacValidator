import setuptools 

with open("README.md", "r") as fh:
	long_description fh.read()

setuptools.setup(name="MacValidator", version="0.0.1", author="Tharun Kumar", author_email="tharuntkji@gmail.com", description="To check if the entered MAC address whose format is valid or not", long_description=long_description, long_description_content_type="text/markdown", url="https://github.com/tharuntk7/MacValidator.git", packages=setuptools.find_packages(), classifiers=["Programming Language :: Python :: 3", "License :: Own License - CopyRights", "Operating System :: OS Independent"],python_requires='>=3.6')