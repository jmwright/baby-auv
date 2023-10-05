import cadquery as cq
import parameters as params
from components.auv_hull import hull
from components.auv_front_clamp import clamp as front_clamp
from components.auv_rear_clamp import clamp as rear_clamp
from components.auv_forward_bulkhead import bulkhead as forward_bulkhead
from components.auv_rear_bulkhead import bulkhead as rear_bulkhead
from components.auv_antenna_extension import extension_tube
from components.auv_cage import cage
from components.auv_depth_nipple import nipple
from components.auv_006_oring import oring
from components.auv_neoprene_gasket import gasket
from components.helpers import append_sys_path, handle_args
from cq_annotate import explode_assembly


def build_auv_assembly():
    """Puts all the components of the assembly together in a CadQuery Assembly object"""

    # Define assembly colors to tell the components apart
    hull_color = cq.Color(0.75, 0.75, 0.75, 0.25)
    clamp_color = cq.Color(0.408, 0.278, 0.553, 1.0)
    cage_color = cq.Color(0.04, 0.5, 0.67, 1.0)
    bulkhead_color = cq.Color(0.565, 0.698, 0.278, 1.0)
    hardware_color = cq.Color(0.996, 0.867, 0.0, 1.0)
    seal_color = cq.Color(0.122, 0.125, 0.133, 1.0)

    # Components of the assembly
    auv_assy = cq.Assembly()

    # Add the body as the fixed, central component
    auv_assy.add(hull(), color=hull_color)

    # Add the forward bulkhead
    auv_assy.add(
        forward_bulkhead(),
        color=bulkhead_color,
        loc=cq.Location((12.0, 0.0, 0.0), (0, 0, 1), 180),
        metadata={"explode_loc": cq.Location((60, 0, 0))},
    )

    # Add the front clamp
    auv_assy.add(
        front_clamp(),
        color=clamp_color,
        loc=cq.Location((-4.0, 0.0, 0.0), (1, 0, 0), 90),
        metadata={"explode_loc": cq.Location((-84, 0, 0))},
    )

    # Add the antenna extension tube
    auv_assy.add(
        extension_tube(params),
        color=hardware_color,
        loc=cq.Location((0.0, 26.0, 0.0), (0, 0, 1), 180),
        metadata={"explode_loc": cq.Location((100, 0, 0))},
    )

    # Add the rear bulkhead
    auv_assy.add(
        rear_bulkhead(params),
        color=bulkhead_color,
        loc=cq.Location((params.hull_length - 12.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((60, 0, 0))},
    )

    # Add the rear clamp
    auv_assy.add(
        rear_clamp(params).rotateAboutCenter((1, 0, 0), 30),
        color=clamp_color,
        loc=cq.Location((params.hull_length - 3.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((80, 0, 0))},
    )

    # Add the cage
    auv_assy.add(
        cage(params),
        color=cage_color,
        loc=cq.Location((params.hull_length + 2.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((100, 0, 0))},
    )

    # Add the depth gauge nipple
    auv_assy.add(
        nipple(params),
        color=hardware_color,
        loc=cq.Location((params.hull_length - 22.0, 9.6, -24.4), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((100, 0, 0))},
    )

    # Add the o-ring for the conductivity sensor
    auv_assy.add(
        oring(),
        color=seal_color,
        loc=cq.Location((params.hull_length - 13.0, -23.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((40, 0, 0))},
    )

    # Add the rear neoprene expansion gasket
    auv_assy.add(
        gasket(),
        color=seal_color,
        loc=cq.Location((params.hull_length - 6.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((71, 0, 0))},
    )

    # Add the forward neoprene expansion gasket
    auv_assy.add(
        gasket(),
        color=seal_color,
        loc=cq.Location((0.0, 0.0, 0.0), (0, 0, 1), 0),
        metadata={"explode_loc": cq.Location((-75, 0, 0))},
    )

    return auv_assy


def document(docs_images_path, manufacturing_files_path):
    """Documents the top level assembly and any sub-assemblies."""
    import os

    assy = build_auv_assembly()

    # Save the stock assembly so it can be viewed online
    assy.save(os.path.join(docs_images_path, "baby_auv_assembly.gltf"))

    # Save the exploded assembly so it can be viewed online
    explode_assembly(assy)
    assy.save(os.path.join(docs_images_path, "baby_auv_exploded_assembly.gltf"))


# In case this is being run from CQ-editor
if "show_object" in globals():
    assy = build_auv_assembly()
    show_object(assy)


def main(args):
    """Main entry point to the app for command line users"""

    # Generate documentation
    if args.document == True:
        import components.helpers as helpers

        docs_images_path = helpers.get_docs_images_path(3)
        manufacturing_files_path = helpers.get_manufacturing_files_path(3)

        document(docs_images_path, manufacturing_files_path)
    # Display the assembly
    else:
        from cadquery.vis import show

        assy = build_auv_assembly()
        # explode_assembly(assy)
        show(assy)


if __name__ == "__main__":
    main(handle_args())
