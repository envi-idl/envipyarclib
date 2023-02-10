;+
; :Description:
;    Task to test task engine ENVIROI datatype
;    See qa_envitaskengine_datatype_enviroi.task for details
;
; :Author:
;    JWD, July, 2018 - Initial Draft
;-
pro qa_envitaskengine_datatype_enviroi, $
  INPUT=input, $
  OUTPUT=output
  compile_opt idl2

  if (~isa(input, 'ENVIROI')) then begin
    Message, 'INPUT is not an ENVIROI'
  endif

  if (Isa(input, /ARRAY)) then begin
    Message, 'INPUT must be scalar'
  endif

  if (Isa(inputRois, 'Collection')) then begin
    Message, 'INPUT_ROIS is a collection, but it should not be'
  endif

  output = input
end
