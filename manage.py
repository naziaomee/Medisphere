#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run administrative tasks."""
    # Use the actual project package name (lowercase) so Django can import settings
    # Make sure the inner project directory is importable. The repository has
    # a nested layout: this top-level folder contains a `MediSphere` directory
    # which holds the `medisphere` Django package. Add it to sys.path so
    # Python can import `medisphere.settings` when this top-level manage.py
    # is executed.
    project_root = os.path.dirname(os.path.abspath(__file__))
    inner_project = os.path.join(project_root, "MediSphere")
    if inner_project not in sys.path:
        sys.path.insert(0, inner_project)

    # Use the actual project package name (lowercase) so Django can import settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medisphere.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
