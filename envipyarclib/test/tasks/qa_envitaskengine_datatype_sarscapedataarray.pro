;+
; :Description:
;    Task to test task engine SARSCAPEDATAARRAY datatype
;    See qa_envitaskengine_datatype_sarscapedataarray.task for details
;
; :Author:
;    JWD, June, 2018 - Initial Draft
;-
pro qa_envitaskengine_datatype_sarscapedataarray, $
  INPUT=input, $
  OUTPUT=output
  compile_opt idl2
  
  if (Isa(input, /SCALAR)) then begin
    Message, 'INPUT is a SCALAR'
  endif

  foreach element, input do begin
    if (~Isa(element, 'SARScapeData')) then begin
      message, 'Element is not of type SARScapeData: ' + String(input)
    endif
  endforeach

  output = input
end
