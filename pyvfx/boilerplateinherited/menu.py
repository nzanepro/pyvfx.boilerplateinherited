from pyvfx.boilerplate import boilerplateUI
try:
    import maya.cmds as cmds
    import pymel.core as pm
    MAYA = True
except ImportError:
    MAYA = False

try:
    import nuke
    NUKE = True
except ImportError:
    NUKE = False


def activate(dockable=False):
    if NUKE:
        from pyvfx.boilerplateinherited.exampleUI import myPlate
        bpr = boilerplateUI.BoilerplateRunner(guiClass=myPlate, win_title='Myplate', win_object='myPlate')
    if MAYA:
        from pyvfx.boilerplateinherited.exampleUI import myPlate2
        bpr = boilerplateUI.BoilerplateRunner(guiClass=myPlate2, win_title='Myplate2', win_object='myPlate2')
    bpr.run_main(dockable)


if NUKE:
    m = nuke.menu("Nuke")
    m.addCommand("pyvfx/inherited boilerplate UI",
                 "import pyvfx.boilerplateinherited.menu\npyvfx.boilerplateinherited.menu.activate()")
    m.addCommand("pyvfx/inherited boilerplate UI dockable",
                 "import pyvfx.boilerplateinherited.menu\npyvfx.boilerplateinherited.menu.activate(True)")

if MAYA:
    MainMayaWindow = pm.language.melGlobals['gMainWindow']
    if not cmds.menu('pyvfxMenuItemRoot', exists=True):
        cmds.menu("pyvfxMenuItemRoot", label="pyvfx", parent=MainMayaWindow,
                  tearOff=True, allowOptionBoxes=True)

    cmds.menuItem(label="inherited boilerplate UI",
                  parent="pyvfxMenuItemRoot", ec=True,
                  command="import pyvfx.boilerplateinherited.menu\npyvfx.boilerplateinherited.menu.activate()")

    cmds.menuItem(label="inherited boilerplate UI dockable",
                  parent="pyvfxMenuItemRoot", ec=True,
                  command="import pyvfx.boilerplateinherited.menu\npyvfx.boilerplateinherited.menu.activate(True)")
