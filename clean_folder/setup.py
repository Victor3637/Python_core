from setuptools import setup, find_namespace_packages

setup(
    name='sorter',
    version='0.0.2',
    description='сортувальник файлів',
    url='http://github.com/dummy_user/useful',
    author='Victor',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sorter']}
)
