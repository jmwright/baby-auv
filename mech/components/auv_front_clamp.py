# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
clamp_od = 88.0  # Outer diameter of the clamp
clamp_id = 60.0  # Inner diameter of the clamp
clamp_thickness = 4.0  # Thickness of the clamp

# Derived parameters
clamp_or = clamp_od / 2.0
clamp_ir = clamp_id / 2.0


def clamp(params):
    """Generates the front clamp of the AUV"""

    # Primary shape of the clamp
    cl = cq.Workplane("YZ").circle(clamp_or).circle(clamp_ir).extrude(clamp_thickness)

    # Add the polar hole pattern
    cl = (
        cl.faces(">X")
        .workplane()
        .polarArray(params.pcd_rad, 60, 360, 6)
        .hole(params.hole_dia)
    )

    # Add the circular notches
    cl = cl.faces(">X").workplane().pushPoints([(0.0, 27.0), (0.0, -27.0)]).hole(10.0)

    return cl


def document(params, docs_images_path, manufacturing_files_path):
    """Allows this model to be documented by itself or part of a larger system"""

    import os

    # Establish standard colors for the SVG line colors
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

    # Generate the extension tube and export drawings for it
    fc = clamp(params)
    final_path = os.path.join(docs_images_path, "front_clamp_right_side_view.svg")
    cq.exporters.export(fc, final_path, opt=opts)


def main(args):
    from helpers import (
        append_sys_path,
        get_docs_images_path,
        get_manufacturing_files_path,
    )

    # Get the paths for the documentation output files
    docs_images_path = get_docs_images_path(3)
    manufacturing_files_path = get_manufacturing_files_path(3)

    append_sys_path(".")
    import parameters as params

    # Generate documentation images and drawings
    if args.document == True:
        document(params, docs_images_path, manufacturing_files_path)
    # Generate and display the model
    else:
        from cadquery.vis import show

        cl = clamp(params)
        show(cl)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
