import argparse
from exsource_tools import tools


def _process_cadquery(export):
    """
    Processes a CadQuery export for display.
    """
    import sys
    import path
    import traceback
    from cadquery import cqgi
    from cadquery.vis import show

    # Get the source files so that they can be executed and displayed
    sources = export.source_files
    params = export.parameters

    # Step through each source file, execute it, and then export its output file(s)
    for source in sources:
        # Read the contents of the source file
        with open(source.filepath) as f: script_code = f.read()

        # In order to load modules in the project directory, we need to add the path to the Python path
        directory = path.Path(source.filepath).abspath()
        base_path = directory.parent
        sys.path.append(base_path)

        # Execute the CadQuery script
        try:
            # Run the script code and get the CadQuery result objects back
            result = cqgi.parse(script_code).build(build_parameters=params)

            # Model execution can fail for a variety of reasons
            if result.success:
                show(result.first_result.shape)
            else:
                # Jump through hoops to keep the exception from being swallowed
                raise result.exception

        except Exception:
            traceback.print_exc()

    print(export)


def main():
     # Set up the parser, telling it what option(s) are available
    parser = argparse.ArgumentParser(
        description="Displays and/or generates documentation and output files for this model."
    )
    parser.add_argument(
        "-d", "--display_method",
        dest="display_method",
        help="Which method to be used to display the open hardware file. 'cq.vis' is currently the only option supported.",
    )
    parser.add_argument(
        "-n", "--export_name",
        dest="export_name",
        help="Which open hardware file should be displayed."
    )

    # Parse the current arguments and pass them back to the caller
    args = parser.parse_args()

    # Handle the requested method properly
    if args.display_method == "cq.vis":
        # The def file needs to be loaded so that we can pull names and parameters
        def_file = tools.load_exsource_file("exsource-def.yaml")

        # Make sure that the requested component is in the ExSource file
        if args.export_name not in def_file.exports.keys():
            print(f"Export {args.export_name} is not in the exsource-def.yaml file.")
            quit(1)

        # Process the def file so that names and parameters can be extracted
        the_export = def_file.exports[args.export_name]
        if the_export.application == "cadquery":
            _process_cadquery(the_export)


if __name__ == "__main__":
    main()