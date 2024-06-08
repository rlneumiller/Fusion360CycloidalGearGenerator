import os

import adsk.core
import adsk.fusion

from ... import config
from ...lib import fusionAddInUtils as futil
from .logic import CycloidalGearLogic

app = adsk.core.Application.get()
ui = app.userInterface

cycloidal_gear_logic: CycloidalGearLogic = None

CMD_ID = f"{config.COMPANY_NAME}_{config.ADDIN_NAME}_cmdDialog"
CMD_NAME = "Cycloidal Gear Generator"
CMD_Description = "A Fusion 360 Add-in for generating cycloidal gear systems"

IS_PROMOTED = True

WORKSPACE_ID = "FusionSolidEnvironment"
PANEL_ID = "SolidScriptsAddinsPanel"
COMMAND_BESIDE_ID = "ScriptsManagerCommand"


ICON_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "")

local_handlers = []


# Executed when add-in is run.
def start():
    futil.log(f"{CMD_NAME} entry.py: Command Start Event")
    
    cmd_definitions = ui.commandDefinitions.addButtonDefinition(
        CMD_ID, CMD_NAME, CMD_Description, ICON_FOLDER
    )
        
    futil.add_handler(cmd_definitions.commandCreated, command_created)

    # ******** Add a button into the UI so the user can run the command. ********
    # Get the target workspace the button will be created in.
    workspace = ui.workspaces.itemById(WORKSPACE_ID)
    panel = workspace.toolbarPanels.itemById(PANEL_ID)
    control = panel.controls.addCommand(cmd_definitions, COMMAND_BESIDE_ID, False)
    control.isPromoted = IS_PROMOTED


# Executed when add-in is stopped.
def stop():
    futil.log(f"{CMD_NAME} entry.py: Command Stop Event")

    # Get the various UI elements for this command
    workspace = ui.workspaces.itemById(WORKSPACE_ID)
    panel = workspace.toolbarPanels.itemById(PANEL_ID)
    command_control = panel.controls.itemById(CMD_ID)
    command_definition = ui.commandDefinitions.itemById(CMD_ID)

    if command_control:
        command_control.deleteMe()

    if command_definition:
        command_definition.deleteMe()


def command_created(args: adsk.core.CommandCreatedEventArgs):
    '''Called when the user clicks the button in the UI.'''

    futil.log(f"{CMD_NAME} entry.py: Command Created Event")
    
    inputs = args.command.commandInputs

    futil.add_handler(
        args.command.execute, command_execute, local_handlers=local_handlers
    )
    futil.add_handler(
        args.command.inputChanged, command_input_changed, local_handlers=local_handlers
    )
    futil.add_handler(
        args.command.executePreview, command_preview, local_handlers=local_handlers
    )
    futil.add_handler(
        args.command.validateInputs,
        command_validate_input,
        local_handlers=local_handlers,
    )
    futil.add_handler(
        args.command.destroy, command_destroy, local_handlers=local_handlers
    )

    des: adsk.fusion.Design = app.activeProduct
    if des is None:
        return

    global cycloidal_gear_logic
    cycloidal_gear_logic = CycloidalGearLogic(des=des)

    cmd = args.command
    cmd.isExecutedWhenPreEmpted = False

    cycloidal_gear_logic.CreateCommandInputs(cmd.commandInputs)

def command_execute(args: adsk.core.CommandEventArgs):
    '''Called when the user clicks the OK button in the command dialog'''
    
    futil.log(f"{CMD_NAME} Command Execute Event")

    cycloidal_gear_logic.HandleExecute(args)

def command_preview(args: adsk.core.CommandEventArgs):
    '''Called when the command needs to compute a new preview in the graphics window.'''
    futil.log(f"{CMD_NAME} Command Preview Event")

def command_input_changed(args: adsk.core.InputChangedEventArgs):
    '''Called when the user changes anything in the command dialog 
    allowing you to modify values of other inputs based on that change.'''
    
    futil.log(f"{CMD_NAME} Input Changed Event fired from a change to {args.input.id}")

    cycloidal_gear_logic.HandleInputsChanged(args)

def command_validate_input(args: adsk.core.ValidateInputsEventArgs):
    '''Called when the user interacts with any of the inputs in the dialog'''

    futil.log(f"{CMD_NAME} Validate Input Event")

    cycloidal_gear_logic.HandleValidateInputs(args)



def command_destroy(args: adsk.core.CommandEventArgs):
    '''Called when the command terminates'''
       
    futil.log(f"{CMD_NAME} Command Destroy Event")

    global local_handlers
    local_handlers = []
