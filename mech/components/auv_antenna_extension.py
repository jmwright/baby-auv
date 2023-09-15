# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
tube_od = 6.0  # mm - Outer diameter of the extension tube
tube_id = 4.0  # mm - Inner diameter of the extension tube
tube_length = 90.0  # mm - Length of the extension tube


def extension_tube(params):
    """Generates the antenna extension tube for the forward bulkhead of the AUV"""

    # Convert diameters to radii
    tube_or = tube_od / 2.0
    tube_ir = tube_id / 2.0

    # Generate the tube
    tube = cq.Workplane("YZ").circle(tube_or).circle(tube_ir).extrude(tube_length)

    return tube


def document(params):
    """Allows this model to be documented by itself or part of a larger system"""

    # Make sure that the helpers module can be found no matter how this is run
    import os
    import sys
    import path

    directory = path.Path(__file__).abspath()
    sys.path.append(directory.parent)
    from helpers import get_docs_images_path, get_manufacturing_files_path

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

    # Get the path to the documentation images and manufacturing output files
    docs_images_path = get_docs_images_path(__file__)
    manufacturing_files_path = get_manufacturing_files_path(__file__)

    # Generate the extension tube and export drawings for it
    et = extension_tube(params)
    final_path = os.path.join(
        docs_images_path, "antenna_extension_tube_right_side_view.svg"
    )
    cq.exporters.export(et, final_path, opt=opts)


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

        et = extension_tube(params)
        show(et)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
