# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
major_dia = 82.5
minor_dia = 72.0
step_heights = 6.0
pcb_hole_dia = 2.5  # Circuit board mounting hole diameter


def bulkhead(params):
    """Generates the forward bulkhead of the AUV"""

    # First step of the shape
    major_rad = major_dia / 2.0
    bh = cq.Workplane("YZ").circle(major_rad).extrude(step_heights)

    # Second step of the shape
    minor_rad = minor_dia / 2.0
    bh = bh.faces(">X").workplane().circle(minor_rad).extrude(step_heights)

    # Add the polar hole pattern
    bh = (
        bh.faces(">X")
        .workplane()
        .polarArray(params.pcd_rad, 30, 360, 6)
        .hole(params.hole_dia, 8.0)
    )

    # Add the antenna hole
    bh = bh.faces(">X").workplane().center(-26.0, 0.0).hole(4.0)

    # Add circuit board mounting holes
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .rarray(18.5 * 2.0, 20.9 * 2.0, 2, 2)
        .hole(pcb_hole_dia, 3.0)
    )

    return bh


def document(params):
    """Allows this model to be documented by itself or part of a larger system"""

    # Make sure that the helpers module can be found no matter how this is run
    import os
    import sys
    import path

    directory = path.Path(__file__).abspath()
    sys.path.append(directory.parent)
    from helpers import get_docs_images_path, get_manufacturing_files_path

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

    # Get the path to the documentation images and manufacturing output files
    docs_images_path = get_docs_images_path(__file__)
    manufacturing_files_path = get_manufacturing_files_path(__file__)

    # Generate the extension tube and export drawings for it
    fb = bulkhead(params)
    final_path = os.path.join(docs_images_path, "forward_bulkhead_right_side_view.svg")
    cq.exporters.export(fb, final_path, opt=opts)


def main(args):
    from helpers import append_sys_path

    append_sys_path(".")
    import parameters as params

    # Generate documentation images and drawings
    if args.document == True:
        document(params)
    # Generate the model and display it
    else:
        from cadquery.vis import show

        bh = bulkhead(params)
        show(bh)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
