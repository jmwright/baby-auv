# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
id = 72  # mm
rect_cross_section = 6  # mm


def gasket():
    """Generates the neoprene expansion gasket"""

    gskt = (
        cq.Workplane("YZ")
        .circle(id / 2.0 + rect_cross_section)
        .circle(id / 2.0)
        .extrude(rect_cross_section)
    )

    return gskt


def document(docs_images_path, manufacturing_files_path):
    """Allows this model to be documented by itself or part of a larger system"""

    import os

    # Standard colors for SVG export
    svg_line_color = (10, 10, 10)
    svg_hidden_color = (127, 127, 127)

    # Standard options for SVG export
    opts = {
        "width": 800,
        "height": None,
        "marginLeft": 10,
        "marginTop": 10,
        "showAxes": False,
        "projectionDir": (1.0, 0.0, 0.0),
        "strokeWidth": 0.5,
        "strokeColor": svg_line_color,
        "hiddenColor": svg_hidden_color,
        "showHidden": False,
    }

    # Generate the depth nipple and export drawings for it
    gskt = gasket()
    final_path = os.path.join(
        docs_images_path, "neoprene_expansion_gasket_right_side_view.svg"
    )
    cq.exporters.export(gskt, final_path, opt=opts)

    # Export an STL of the depth nipple in case that is the manufacturing method
    final_path = os.path.join(manufacturing_files_path, "neoprene_expansion_gasket.stl")
    cq.exporters.export(gskt, final_path)


def main(args):
    from helpers import (
        get_docs_images_path,
        get_manufacturing_files_path,
    )

    # Get the paths for the documentation output files
    docs_images_path = get_docs_images_path(3)
    manufacturing_files_path = get_manufacturing_files_path(3)

    # Generate documentation images and drawings
    if args.document == True:
        document(docs_images_path, manufacturing_files_path)
    # Generate the model and display it
    else:
        from cadquery.vis import show

        gskt = gasket()
        show(gskt)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
