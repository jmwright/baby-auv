import os
import cadquery as cq
# from cq_annotate import add_circular_dimensions
from components.auv_hull import document as hull_document
from components.auv_rear_clamp import document as rear_clamp_document

svg_line_color = (10, 10, 10)
svg_hidden_color = (127, 127, 127)

def export_drawings(params):
    """
    Handles creating dimensioned SVG drawings of components.
    """

    # The body
    bd = hull_document(params)
    fbh = rear_clamp_document(params)
    # bd = add_circular_dimensions(bd, arrow_scale_factor=0.25)


def document(base_dir, functions):
    # Create the docs/images directory if it does not exist
    docs_images_path = os.path.join(base_dir, "docs", "images")
    exists = os.path.exists(docs_images_path)
    if not exists:
        os.makedirs(docs_images_path)

    # Create the docs/output/stl directory if it does not exist
    docs_output_path = os.path.join(base_dir, "docs", "manufacturing_files")
    exists = os.path.exists(docs_output_path)
    if not exists:
        os.makedirs(docs_output_path)

    import parameters as params

    # Export any dimensioned manufacturing drawings that are desired
    export_drawings(params)

    print("Documenting...")
