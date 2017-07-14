

pro CreateGPToolbox, SERVICE_URL=serviceUrl, $
                     SERVICE_NAME=serviceName, $
                     TASK_NAMES=taskNames, $
                     TOOLBOX_NAME=toolboxName, $
                     OUTPUT_TOOLBOX_DIR=outputToolboxDir
  compile_opt idl2
  
  cmd = 'C:/Development/services_engine/client/python/gsfarc/gsfarc/server/creategptoolbox.py '
  
  args = serviceUrl + ' '
  args += serviceName + ' '
  foreach taskName, taskNames do begin
    args += taskName + ' '
  endforeach
  
  if (N_Elements(toolboxName) gt 0) then begin
    args += '--toolbox_name ' + toolboxName + ' '
  endif
  
  if (N_Elements(outputToolboxDir) gt 0) then begin
    args += '--directory "' + outputToolboxDir + '" '
  endif
  
  cmd += args
  print, cmd
  
  spawn, cmd, result, EXIT_STATUS=exitStatus, /STDERR, /HIDE
  if (exitStatus ne 0) then begin
    message, 'Failed to create toolbox: ' + strjoin(result)
  endif

end