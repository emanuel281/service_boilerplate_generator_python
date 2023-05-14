"""
Generate boilerplate folder structure and files for creating a service/module.
"""
import os
import io
from pathlib import Path
import sys


def generate_boilerplate(project_name: str, directory: Path = None, encoding: str = 'utf-8'):
    """
    Generate boilerplate files and folders
    """
    main_folder = (directory or Path(__file__).parent.parent) / project_name
    os.mkdir(main_folder)

    build_files = [
        ('setup.py', '"""Setup file"""\n'),
        ('Dockerfile', ''),
        ('README.md', f'"""{project_name} README.md"""\n'),
        ('.dockerignore', ''),
    ]

    for file, description in build_files:
        with io.open(main_folder / file, 'w', encoding=encoding) as file_p:
            file_p.write(description)

    main_folder = main_folder / project_name
    boiler_folders = [
        (main_folder, '"""Main module"""\n'),
        (main_folder / 'models', '"""Models module"""\n'),
        (main_folder / 'clients', '"""Clients folder for interacting with 3rd party services"""\n'),
        (main_folder / 'resources', '"""Handlers or endpoint logic"""\n'),
        (main_folder / 'scripts', '"""Scripts for deploy, build, etc"""\n'),
        (main_folder / 'tests', '"""Tests module"""\n'),
        (main_folder / 'tests/fixtures', '"""Fixtures module"""\n'),
        (main_folder / 'tests/functional', '"""Functional tests module"""\n'),
        (main_folder / 'tests/unit', '"""Unit tests module"""\n'),
    ]

    for folder, description in boiler_folders:
        main_folder = main_folder / folder
        os.mkdir(main_folder)
        with io.open(main_folder / '__init__.py', 'w', encoding=encoding) as file_p:
            file_p.write(description)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(f'\n{Path(__file__).name} <project_name>', end='\n\n')
        exit()

    PROJECT_NAME = sys.argv[1].lower().replace(' ', '_')

    generate_boilerplate(PROJECT_NAME)
