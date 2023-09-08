import path
import os
import sys
import argparse


def append_sys_path(proj_path):
    """Handles appending the main parent directory to the sys path so parameters can be imported"""

    # Make sure Python can find the import file
    directory = path.Path(__file__).abspath()
    return sys.path.append(directory.parent.parent)


def handle_args():
    """Allows the user to pass the document argument to generate the documentation materials."""

    # Set up the parser, telling it what option(s) are available
    parser = argparse.ArgumentParser(
        description="Displays and/or generates documentation and output files for this model."
    )
    parser.add_argument(
        "--document",
        dest="document",
        action="store_true",
        help="Tells the app whether or not to generate documentation and output files. If present, the model will not be displayed in a window.",
    )

    # Parse the current arguments and pass them back to the caller
    args = parser.parse_args()
    return args


def get_docs_images_path(base_path):
    """Gets the documentation images path for the user, creating the directory if needed"""

    # Handle wanting the parent directory
    if "components" in base_path:
        # We need to go up an extra directory to get to the base
        directory = path.Path(__file__).abspath()
        base_path = directory.parent.parent.parent
    else:
        directory = path.Path(__file__).abspath()
        base_path = directory.parent.parent

    # Create the docs/images directory if it does not exist
    docs_images_path = os.path.join(base_path, "docs", "images")
    if os.path.exists(docs_images_path) is not True:
        os.makedirs(docs_images_path)

    return docs_images_path


def get_manufacturing_files_path(base_path):
    # Handle wanting the parent directory
    if "components" in base_path:
        directory = path.Path(__file__).abspath()
        base_path = directory.parent.parent.parent
    else:
        directory = path.Path(__file__).abspath()
        base_path = directory.parent.parent

    # Create the docs/output/stl directory if it does not exist
    docs_output_path = os.path.join(base_path, "docs", "manufacturing_files")
    if os.path.exists(docs_output_path) is not True:
        os.makedirs(docs_output_path)

    return docs_output_path
