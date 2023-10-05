# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
straight_length = 25.0  # mm
barb_half_length = 5.0  # mm
tube_od = 4.0  # mm
tube_id = 2.0  # mm
barb_od = 4.9  # mm
barb_length = 5.0  # mm


def nipple():
    """Generates the nipple for the depth sensor tube."""

    # Main tube shape
    np = cq.Workplane("YZ").circle(tube_od / 2.0).extrude(straight_length)

    # Hose barb
    np = (
        np.faces(">X")
        .workplane()
        .circle(barb_od / 2.0)
        .extrude(barb_length, taper=-174.75)
    )

    # Post-barb tube
    np = np.faces(">X").workplane().circle(tube_od / 2.0).extrude(2.0)

    # Center hole
    np = np.faces(">X").workplane().circle(tube_id / 2.0).cutThruAll()

    return np


show_object(nipple())

# def document(params, docs_images_path, manufacturing_files_path):
#     """Allows this model to be documented by itself or part of a larger system"""

#     import os

#     # Standard colors for SVG export
#     svg_line_color = (10, 10, 10)
#     svg_hidden_color = (127, 127, 127)

#     # Standard options for SVG export
#     opts = {
#         "width": 800,
#         "height": None,
#         "marginLeft": 10,
#         "marginTop": 10,
#         "showAxes": False,
#         "projectionDir": (1.0, 0.0, 0.0),
#         "strokeWidth": 0.5,
#         "strokeColor": svg_line_color,
#         "hiddenColor": svg_hidden_color,
#         "showHidden": False,
#     }

#     # Generate the depth nipple and export drawings for it
#     np = nipple(params)
#     final_path = os.path.join(docs_images_path, "depth_nipple_right_side_view.svg")
#     cq.exporters.export(np, final_path, opt=opts)

#     # Export an STL of the depth nipple in case that is the manufacturing method
#     final_path = os.path.join(manufacturing_files_path, "depth_nipple.stl")
#     cq.exporters.export(np, final_path)


# def main(args):
#     from helpers import (
#         append_sys_path,
#         get_docs_images_path,
#         get_manufacturing_files_path,
#     )

#     # Get the paths for the documentation output files
#     docs_images_path = get_docs_images_path(3)
#     manufacturing_files_path = get_manufacturing_files_path(3)

#     append_sys_path(".")
#     import parameters as params

#     # Generate documentation images and drawings
#     if args.document == True:
#         document(params, docs_images_path, manufacturing_files_path)
#     # Generate the model and display it
#     else:
#         from cadquery.vis import show

#         np = nipple(params)
#         show(np)


# if __name__ == "__main__":
#     from helpers import handle_args

#     main(handle_args())
