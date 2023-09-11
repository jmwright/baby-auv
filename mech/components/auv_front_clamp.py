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
    cl = (
        cl.faces(">X")
        .workplane()
        .pushPoints([(0.0, 27.0), (0.0, -27.0)])
        .hole(10.0)
    )

    # 27.0 mm
    # 10.0 mm dia

    return cl


def main(args):
    from helpers import append_sys_path

    append_sys_path(".")
    import parameters as params

    # Generate documentation images and drawings
    if args.document == True:
        document(params)
    # Generate and display the model
    else:
        from cadquery.vis import show

        cl = clamp(params)
        show(cl)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
