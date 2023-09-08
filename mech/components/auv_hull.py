# All units are in mm unless otherwise stated

import cadquery as cq


def hull(params):
    """Generates the main hull tube of the AUV"""

    # Convert diameter to radius
    hull_radius = params.hull_diameter / 2.0

    # The overall tube shape
    hl = (
        cq.Workplane("YZ")
        .circle(hull_radius)
        .circle(hull_radius - params.hull_wall_thickness)
        .extrude(params.hull_length)
    )

    # Tag edges for dimensioning
    hl.edges("%CIRCLE").edges(cq.selectors.RadiusNthSelector(1)).edges(">X").tag(
        "radius_1"
    )

    return hl


def document(params):
    """Allows this model to be documented by itself or part of a larger system"""

    # Make sure that the helpers module can be found no matter how this is run
    import os
    import sys
    import path

    directory = path.Path(__file__).abspath()
    sys.path.append(directory.parent)
    from helpers import get_docs_images_path, get_manufacturing_files_path

    # Set standard SVG output line colors
    svg_line_color = (10, 10, 10)
    svg_hidden_color = (127, 127, 127)

    # Standard SVG output options
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

    # Generate the model so it can be exported
    bd = hull(params)

    # Export the end view of the hull tube in SVG
    # bd = add_circular_dimensions(bd, arrow_scale_factor=0.25)
    final_path = os.path.join(docs_images_path, "hull_right_side_view.svg")
    cq.exporters.export(bd, final_path, opt=opts)

    # Export the end view of the hull tube in DXF
    final_path = os.path.join(manufacturing_files_path, "hull_right_side_view.dxf")
    cq.exporters.export(bd, final_path)


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

        hl = hull(params)
        show(hl)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
