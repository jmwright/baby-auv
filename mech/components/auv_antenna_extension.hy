; All units are in mm unless otherwise stated

(import hy)
(import cadquery :as cq)

(setv tube_od 6.0) ; mm - Outer diameter of the extension tube
(setv tube_id 4.0) ; mm - Inner diameter of the extension tube
(setv tube_length 90.0) ; mm - Length of the extension tube


(defn extension_tube [params]
    "Generates the antenna extension tube for the forward bulkhead of the AUV"

    ; Convert diameters to radii
    (setv tube_or (/ tube_od 2.0))
    (setv tube_ir (/ tube_id 2.0))

    ; Generate the tube
    (setv tube (.extrude (.circle (.circle (cq.Workplane "YZ") tube_or) tube_ir) tube_length))

    (return tube)
)


(defn document [params]
    "Allows this model to be documented by itself or part of a larger system"

    ; Make sure that the helpers module can be found no matter how this is run
    (import os)
    (import sys)
    (import path)
    (setv directory (.abspath (path.Path __file__)))
    (sys.path.append directory.parent)

    (import helpers [get_docs_images_path get_manufacturing_files_path])

    (setv svg_line_color #(10 10 10))
    (setv svg_hidden_color #(127 127 127))
)


(defn main [args]
    (import helpers [append_sys_path])
    (append_sys_path ".")
    (import parameters :as params)

    (if (= args.document True)
        (document params)
        (do
            (import cadquery.vis [show])

            ; Generate the model and display it
            (setv et (extension_tube params))
            (show et)
        )
    )
)


(if (= __name__ "__main__")
    (do
        (import helpers [handle_args])
        (main (handle_args))
    )
    None
)
