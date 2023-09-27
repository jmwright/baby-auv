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
from components.auv_depth_nipple import document as depth_nipple_document


def document():
    print("Documenting...")

    import components.helpers as helpers

    docs_images_path = helpers.get_docs_images_path(3)
    manufacturing_files_path = helpers.get_manufacturing_files_path(3)

    import parameters as params

    # Export the entire assembly
    assy_document(docs_images_path, manufacturing_files_path)

    # Export individual components of the assembly
    hull_document(params, docs_images_path, manufacturing_files_path)
    rear_clamp_document(params, docs_images_path, manufacturing_files_path)
    ant_extension_document(params, docs_images_path, manufacturing_files_path)
    front_clamp_document(params, docs_images_path, manufacturing_files_path)
    bulkhead_document(params, docs_images_path, manufacturing_files_path)
    cage_document(params, docs_images_path, manufacturing_files_path)
    rear_bulkhead_document(params, docs_images_path, manufacturing_files_path)
    depth_nipple_document(params, docs_images_path, manufacturing_files_path)

    print("finished documenting.")


if __name__ == "__main__":
    document()
