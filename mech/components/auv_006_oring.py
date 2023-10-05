# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
od = 6.35  # mm (1/4 in)
id = 2.9  # mm
cross_section = 1.78  # mm


def oring():
    # Overall ring shape
    ring = (
        cq.Workplane("YZ")
        .circle(id / 2.0 + cross_section)
        .circle(id / 2.0)
        .extrude(cross_section)
    )

    # Fillets to make it more o-ring shaped
    ring = ring.edges().fillet(cross_section / 2.0 - 0.001)

    return ring


show_object(oring())
