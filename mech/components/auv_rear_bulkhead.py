# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
major_dia = 82.5
minor_dia = 72.0
step_heights = 6.0


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

    return bh


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
