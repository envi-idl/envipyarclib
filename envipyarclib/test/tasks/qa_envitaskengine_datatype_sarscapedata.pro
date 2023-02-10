;+
; :Description:
;    Task to test task engine SARSCAPEDATA datatype
;    See qa_envitaskengine_datatype_sarscapedata.task for details
;
; :Author:
;    JWD, June, 2018 - Initial Draft
;-
pro qa_envitaskengine_datatype_sarscapedata, $
  INPUT=input, $
  OUTPUT=output
  compile_opt idl2

  if (~Isa(input, 'SARScapeData')) then begin
    Message, 'INPUT is not of type: SARScapeData'
  endif
  
  output = input
end
