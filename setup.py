import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="limit_memory_usage",
    version="0.0.1",
    author="Jonathan Oakey",
    author_email="jonathandoakey@gmail.com",
    description="This will limit the memory usage of your python function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonoak/limit_memory_usage.git",
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    py_modules=['limit_memory_usage'],
      scripts=['limit_memory_usage.py'],
    keywords='limit memory usage'
)