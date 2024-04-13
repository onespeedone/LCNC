
def processed_key_event__(self,receiver,event,is_pressed,key,code,shift,cntrl):
# when typing in MDI, we don't want keybinding to call functions
# so we catch and process the events directly.
# We do want ESC, F1 and F2 to call keybinding functions though
if code not in(QtCore.Qt.Key_Escape,QtCore.Qt.Key_F1 ,QtCore.Qt.Key_F2):
# QtCore.Qt.Key_F3,QtCore.Qt.Key_F4,QtCore.Qt.Key_F5):

# search for the top widget of whatever widget received the event
# then check if it's one we want the keypress events to go to
print ("(Got to Keybind") ##DKS:
flag = False
receiver2 = receiver
while receiver2 is not None and not flag:
if isinstance(receiver2, QtWidgets.QDialog):
flag = True
break
if isinstance(receiver2, QtWidgets.QLineEdit):
flag = True
print ("Line Edit")
break
if isinstance(receiver2, MDI_WIDGET):
flag = True
break
if isinstance(receiver2, GCODE):
print ("Gcode")
flag = True
break
if isinstance(receiver2, TOOL_TABLE):
flag = True
break
if isinstance(receiver2, OFFSET_VIEW):
flag = True
break
receiver2 = receiver2.parent()

if flag:
if isinstance(receiver2, GCODE):
# if in manual or in readonly mode do our keybindings - otherwise
# send events to gcode widget
print("########") ##DKS:
print(STATUS.is_auto_running()) ##DKS:
print(receiver2.isReadOnly()) ##DKS:
## DKS: if STATUS.is_man_mode() == False or not receiver2.isReadOnly():
if (STATUS.is_auto_running() == False) and (STATUS.is_man_mode() == False or not receiver2.isReadOnly()):

print ("Not Man Mode") ##DKS:
print (STATUS.is_man_mode()) ##DKS:
if is_pressed:
print (IsPressed) ##DKS:
receiver.keyPressEvent(event)
event.accept()
return True
elif is_pressed: ## DKS: was if not elif
receiver.keyPressEvent(event)
event.accept()
return True
else:
event.accept()
return True

if event.isAutoRepeat():return True

# ok if we got here then try keybindings function calls
# KEYBINDING will call functions from handler file as
# registered by KEYBIND.add_call(KEY,FUNCTION) above
print ("(Got to Keybind2") ##DKS:

return KEYBIND.manage_function_calls(self,event,is_pressed,key,shift,cntrl)