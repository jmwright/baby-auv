# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
cage_od = 88.9  # mm
cage_id = 84.9  # mm
cage_length = 82.0  # mm
slot_dia = 25.0  # mm
mounting_hole_od = 3.4  # mm

# Derived parameters
cage_or = cage_od / 2.0
cage_ir = cage_id / 2.0
slot_length = 42.0 + slot_dia
mounting_hole_or = mounting_hole_od / 2.0


def cage(params):
    """Generates the cage on the rear clamp of the AUV"""

    # General shape
    cg = cq.Workplane("YZ").circle(cage_or).circle(cage_ir).extrude(cage_length)

    # Add the first pair of slots
    cg = (
        cg.workplane(centerOption="CenterOfBoundBox")
        .transformed(rotate=cq.Vector(0, 90, 0))
        .slot2D(slot_length, slot_dia)
        .cutThruAll()
    )

    # Add the second pair of slots
    cg = (
        cg.workplane(centerOption="CenterOfBoundBox")
        .transformed(rotate=cq.Vector(60, 0, 0))
        .slot2D(slot_length, slot_dia)
        .cutThruAll()
    )

    # Add the third pair of slots
    cg = (
        cg.workplane(centerOption="CenterOfBoundBox")
        .transformed(rotate=cq.Vector(-120, 0, 0))
        .slot2D(slot_length, slot_dia)
        .cutThruAll()
    )

    # Add the first pair of mounting holes
    cg = (
        cg.workplane(centerOption="CenterOfBoundBox")
        .transformed(rotate=cq.Vector(30, 0, 0))
        .center(cage_length / 2.0 - 3.0, 0.0)
        .circle(mounting_hole_or)
        .cutThruAll()
    )

    # Add the second pair of mounting holes
    cg = (
        cg.workplane(centerOption="CenterOfBoundBox")
        .transformed(rotate=cq.Vector(120, 0, 0))
        .center(cage_length / 2.0 - 3.0, 0.0)
        .circle(mounting_hole_or)
        .cutThruAll()
    )

    return cg


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

        cg = cage(params)
        show(cg)


if __name__ == "__main__":
    from helpers import handle_args

    main(handle_args())
