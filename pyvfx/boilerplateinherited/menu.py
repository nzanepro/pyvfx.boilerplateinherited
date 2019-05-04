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
    from pyvfx.boilerplateinherited.exampleUI import myPlate
    bpr = boilerplateUI.BoilerplateRunner(guiClass=myPlate, win_title='Myplate', win_object='myPlate')
    kwargs = {}
    kwargs["dockable"] = dockable
    bpr.run_main(**kwargs)


if NUKE:
    m = nuke.menu("Nuke")
    m.addCommand("pyvfx/inherited boilerplate UI",
                 "import pyvfx.boilerplateinherited.menu\npyvfx.boilerplateinherited.menu.activate()")
    m.addCommand("pyvfx/inherited boilerplate UI dockable",
                 "import pyvfx.boilerplateinherited.menu\npyvfx.boilerplateinherited.menu.activate(True)")

elif MAYA:
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

else:
    activate()
