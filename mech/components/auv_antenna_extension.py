# All units are in mm unless otherwise stated

import cadquery as cq

# Parameters
tube_od = 6.0  # mm - Outer diameter of the extension tube
tube_id = 4.0  # mm - Inner diameter of the extension tube
tube_length = 90.0  # mm - Length of the extension tube


def extension_tube():
    """Generates the antenna extension tube for the forward bulkhead of the AUV"""

    # Convert diameters to radii
    tube_or = tube_od / 2.0
    tube_ir = tube_id / 2.0

    # Generate the tube
    tube = cq.Workplane("YZ").circle(tube_or).circle(tube_ir).extrude(tube_length)

    return tube


show_object(extension_tube())
