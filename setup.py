from setuptools import setup, find_namespace_packages

setup(
    name='virtual-assistant-v007',
    version='0.0.6',
    description='Personal assistant helps you organize your notes and address book.',
    url='https://github.com/basilegupov/personal-notebook',
    author='Olds coders',
    author_email='flyingcircus@example.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    data_files=[('virtual_assistant_v007', ['virtual_assistant_v007/contacts.json', 'virtual_assistant_v007/notes.json'])],
    include_package_data=True,
    package_data={"virtual_assistant_v007": ["*.json", "*.txt"]},
    install_requires=[
        'prompt-toolkit>=3.0'],
    entry_points={'console_scripts': ['run-assistant = virtual_assistant_v007.main:run_bot']},
    zip_safe=False
)
