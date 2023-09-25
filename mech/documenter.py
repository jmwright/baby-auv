import os
import cadquery as cq
from components.helpers import get_docs_images_path, get_manufacturing_files_path

# from cq_annotate import add_circular_dimensions
from baby_auv import document as assy_document
from components.auv_hull import document as hull_document
from components.auv_rear_clamp import document as rear_clamp_document
from components.auv_antenna_extension import document as ant_extension_document
from components.auv_front_clamp import document as front_clamp_document
from components.auv_forward_bulkhead import document as bulkhead_document
from components.auv_cage import document as cage_document
from components.auv_rear_bulkhead import document as rear_bulkhead_document

svg_line_color = (10, 10, 10)
svg_hidden_color = (127, 127, 127)


def export_drawings(params, docs_images_path, docs_output_path):
    """
    Handles creating dimensioned SVG drawings of components.
    """

    # Entire assembly
    assy_document(docs_images_path, docs_output_path)

    # Individual components of the assembly
    hull_document(params)
    rear_clamp_document(params)
    ant_extension_document(params)
    front_clamp_document(params)
    bulkhead_document(params)
    cage_document(params)
    rear_bulkhead_document(params)


def document(base_dir):
    # Create the docs/images directory if it does not exist
    docs_images_path = os.path.join(base_dir, "docs", "images", "generated")
    exists = os.path.exists(docs_images_path)
    if not exists:
        os.makedirs(docs_images_path)

    # Create the docs/output/stl directory if it does not exist
    manufacturing_files_path = os.path.join(base_dir, "docs", "manufacturing_files", "generated")
    exists = os.path.exists(manufacturing_files_path)
    if not exists:
        os.makedirs(manufacturing_files_path)

    import parameters as params

    # Export any dimensioned manufacturing drawings that are desired
    export_drawings(params, docs_images_path, manufacturing_files_path)

    print("Documenting...")


if __name__ == "__main__":
    document("..")
