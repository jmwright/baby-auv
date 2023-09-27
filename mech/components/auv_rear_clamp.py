# All units are in mm unless otherwise stated

import cadquery as cq


def clamp(params):
    """Generates the rear clamp of the AUV"""

    # Outer and inner radii of the first step
    step_1_or = 82.5 / 2.0
    step_1_ir = 72.5 / 2.0

    # Outer and inner radii of the second step
    step_2_or = 88.0 / 2.0
    step_2_ir = 59.5 / 2.0

    # Outer and inner radii of the third step
    step_3_or = 84.0 / 2.0
    step_3_ir = 59.5 / 2.0

    # Outer and inner radii of the forth step
    step_4_or = 84.0 / 2.0
    step_4_ir = 76.0 / 2.0

    # First step of the rear clamp that slips inside the body tube
    rc = cq.Workplane("YZ").circle(step_1_or).circle(step_1_ir).extrude(3.0)

    # Second step of the rear clamp
    rc = rc.faces(">X").workplane().circle(step_2_or).circle(step_2_ir).extrude(2.0)

    # Third step of the rear clamp
    rc = rc.faces(">X").workplane().circle(step_3_or).circle(step_3_ir).extrude(1.0)

    # Forth step of the rear clamp
    rc = rc.faces(">X").workplane().circle(step_4_or).circle(step_4_ir).extrude(6.0)

    # Add the polar hole pattern
    rc = (
        rc.faces(">X")
        .workplane()
        .polarArray(params.pcd_rad, 60, 360, 6)
        .hole(params.hole_dia)
    )

    # Add the cage mounting hole pattern
    mounting_hole_or = params.m3_tap_drill_size / 2.0
    rc = (
        rc.workplane(
            centerOption="CenterOfBoundBox", offset=3.0 - mounting_hole_or / 2.0
        )
        .transformed(rotate=cq.Vector(90, 30, 0))
        .circle(mounting_hole_or)
        .cutThruAll()
    )
    rc = (
        rc.transformed(rotate=cq.Vector(0, 60, 0)).circle(mounting_hole_or).cutThruAll()
    )
    rc = (
        rc.transformed(rotate=cq.Vector(0, -120, 0))
        .circle(mounting_hole_or)
        .cutThruAll()
    )

    return rc


def document(params, docs_images_path, manufacturing_files_path):
    """Allows this model to be documented by itself or part of a larger system"""

    import os

    # Standard line colors for SVG export
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

    # Generate the clamp so it can be exported
    cl = clamp(params)

    # Export the end view of the body tube in SVG
    final_path = os.path.join(docs_images_path, "rear_clamp_right_side_view.svg")
    cq.exporters.export(cl, final_path, opt=opts)

    # Export the end view of the body tube in DXF
    final_path = os.path.join(
        manufacturing_files_path, "rear_clamp_right_side_view.dxf"
    )
    cq.exporters.export(cl, final_path)


def main(args):
    from helpers import append_sys_path, get_docs_images_path, get_manufacturing_files_path

    append_sys_path(".")
    import parameters as params

    # Generate documentation images and drawings
    if args.document == True:
        # Get the paths for the documentation output files
        docs_images_path = get_docs_images_path(3)
        manufacturing_files_path = get_manufacturing_files_path(3)

        document(params, docs_images_path, manufacturing_files_path)
    # Generate and display the model
    else:
        from cadquery.vis import show

        cl = clamp(params)
        show(cl)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
