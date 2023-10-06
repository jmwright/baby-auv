# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
major_dia = 82.5
minor_dia = 72.0
step_heights = 6.0
pcd_rad = 33.0  # mm - Bulkhead hole pattern radius
hole_dia = 3.25  # mm - Bulkhead clearance hole diameter


def bulkhead():
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
        .workplane(centerOption="CenterOfBoundBox")
        .polarArray(pcd_rad, 30, 360, 6)
        .hole(hole_dia, 8.0)
    )

    # Thruster gland hole
    # bh = (
    #     bh.faces("<X")
    #     .workplane(centerOption="CenterOfBoundBox")
    #     .center(23.0, 0.0)
    #     .hole(3.0)
    # )

    # Thruster gland O-ring pocket
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .center(23.0, 0.0)
        .hole(8.0)  # , depth=0.8
    )

    # Thruster gland mount holes
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .center(23.0, 0.0)
        .polarArray(radius=7.0, startAngle=0.0, angle=360.0, count=3)
        .hole(2.5, depth=4.0)
    )

    # Motor mount holes
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .pushPoints([(38.0, 0.0), (23.0, 18.0), (23.0, -18.0)])
        .hole(2.5, depth=4.0)
    )

    # Conductivity sensor pocket and hole
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .center(-12.0, 20.8)
        .hole(18.0, depth=1.8)
        .faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .center(-12.0, 20.8)
        .hole(12.8)
    )

    # Conductivity sensor mounting holes
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .center(-12.0, 20.8)
        .polarArray(radius=13.0, startAngle=30.0, angle=360.0, count=3)
        .hole(3.3, depth=4.0)
    )

    # Depth tube hole
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .center(-9.6, -24.4)
        .hole(4.9)
    )

    # Other mounting holes
    bh = (
        bh.faces("<X")
        .workplane(centerOption="CenterOfBoundBox")
        .pushPoints([(-19.0, -5.0), (-28.0, -5.0), (-25.9, -20.8), (-5.1, -32.8)])
        .hole(2.5, depth=4.0)
    )

    return bh


if "show_object" in globals() or __name__ == "__cqgi__":
    show_object(bulkhead())
