"""checker_colorspace script by Emilio Sarabia Valverde
--------------------------------------------
june 6th, 2024 --version v1.0"""


import nuke

def checker_colorspace():
    all_nodes = nuke.selectAll()
    user_choice = nuke.choice("Colorspace choice","Select the Colorspace for the  Read",["linear","rec709","sRGB","Cineon","Panalog","REDLog","AlexaV3LogC"])
    colorspace_choice = {0:"linear",
                         1:"rec709",
                         2:"sRGB",
                         3:"Cineon",
                         4:"Panalog",
                         5:"REDLog",
                         6:"AlexaV3LogC",
                        }
    
    allread = nuke.selectedNodes("Read")
    
    for n in allread:
        if n.knob("colorspace").value().startswith("Output"):
            n.knob("colorspace").setValue(colorspace_choice[user_choice])
            
    [i.setSelected(False) for i in nuke.allNodes()]
            
    return
    
    
nuke.menu("Nuke").addCommand("Edit/Checker_Colorspace",checker_colorspace,shortcut = "Ctrl+T")
