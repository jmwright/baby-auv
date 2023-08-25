(import path)
(import os)
(import sys)
(import argparse)


(defn append_sys_path [proj_path]
    "Handles appending the main parent directory to the sys path so parameters can be imported"

    ; Make sure Python can find the import file
    (setv directory (.abspath (path.Path __file__)))
    (sys.path.append directory.parent.parent)
)


(defn handle_args []
    "Allows the user to pass the document argument to generate the documentation materials."

    ; Set up the parser, telling it what option(s) are available
    (setv parser (argparse.ArgumentParser :description "Displays and/or generates documentation and output files for this model."))
    (parser.add_argument "--document" :dest "document" :action "store_true" :help "Tells the app whether or not to generate documentation and output files. If present, the model will not be displayed in a window.")

    ; Parse the current arguments and pass them back to the caller
    (setv args (parser.parse_args))
    (return args)
)


(defn get_docs_images_path [base_path]
    "Gets the documentation images path for the user, creating the directory if needed"

    ; Handle wanting the parent directory
    (if (in "components" base_path)
        ; We need to go up an extra directory to get to the base
        (do
            (setv directory (.abspath (path.Path __file__)))
            (setv base_path directory.parent.parent.parent)
        )
        (do
            (setv directory (.abspath (path.Path __file__)))
            (setv base_path directory.parent.parent)
        )
    )

    ; Create the docs/images directory if it does not exist
    (setv docs_images_path (os.path.join base_path "docs" "images"))
    (if (is-not (os.path.exists docs_images_path) True)
        (os.makedirs docs_images_path)
        None
    )

    (return docs_images_path)
)


(defn get_manufacturing_files_path [base_path]
    ; Handle wanting the parent directory
    (if (in "components" base_path)
        ; We need to go up an extra directory to get to the base
        (do
            (setv directory (.abspath (path.Path __file__)))
            (setv base_path directory.parent.parent.parent)
        )
        (do
            (setv directory (.abspath (path.Path __file__)))
            (setv base_path directory.parent.parent)
        )
    )

    ; Create the docs/output/stl directory if it does not exist
    (setv docs_output_path (os.path.join base_path "docs" "manufacturing_files"))
    (if (is-not (os.path.exists docs_output_path) True)
        (os.makedirs docs_output_path)
        None
    )

    (return docs_output_path)
)