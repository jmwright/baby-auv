# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
clamp_od = 88.0  # Outer diameter of the clamp
clamp_id = 60.0  # Inner diameter of the clamp
clamp_thickness = 4.0  # Thickness of the clamp
pcd_rad = 33.0  # mm - Bulkhead hole pattern radius
hole_dia = 3.25  # mm - Bulkhead clearance hole diameter

# Derived parameters
clamp_or = clamp_od / 2.0
clamp_ir = clamp_id / 2.0


def clamp():
    """Generates the front clamp of the AUV"""

    # Primary shape of the clamp
    cl = cq.Workplane("YZ").circle(clamp_or).circle(clamp_ir).extrude(clamp_thickness)

    # Add the polar hole pattern
    cl = (
        cl.faces(">X")
        .workplane()
        .polarArray(pcd_rad, 60, 360, 6)
        .hole(hole_dia)
    )

    # Add the circular notches
    cl = cl.faces(">X").workplane().pushPoints([(0.0, 27.0), (0.0, -27.0)]).hole(10.0)

    return cl


if "show_object" in globals() or __name__ == "__cqgi__":
    show_object(clamp())
