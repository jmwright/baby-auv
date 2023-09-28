# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
od = 6.35  # mm (1/4 in)
id = 2.9  # mm
cross_section = 1.78  # mm


def oring():
    # Overall ring shape
    ring = cq.Workplane("YZ").circle(id / 2.0 + cross_section).circle(id / 2.0).extrude(cross_section)

    # Fillets to make it more o-ring shaped
    ring = ring.edges().fillet(cross_section / 2.0 - 0.001)

    return ring


def document(params, docs_images_path, manufacturing_files_path):
    """Dummy document code"""
    pass


def main(args):
    from helpers import (
        append_sys_path,
        get_docs_images_path,
        get_manufacturing_files_path,
    )

    # Get the paths for the documentation output files
    docs_images_path = get_docs_images_path(3)
    manufacturing_files_path = get_manufacturing_files_path(3)

    # Generate documentation images and drawings
    if args.document == True:
        document(None, docs_images_path, manufacturing_files_path)
    # Generate the model and display it
    else:
        from cadquery.vis import show

        ring = oring()
        show(ring)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
