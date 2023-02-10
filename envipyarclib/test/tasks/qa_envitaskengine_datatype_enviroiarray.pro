;+
; :Description:
;    Task to test task engine ENVIROIARRAY datatype
;    See qa_envitaskengine_datatype_enviroiarray.task for details
;
; :Author:
;    JWD, June, 2018 - Initial Draft
;-
pro qa_envitaskengine_datatype_enviroiarray, $
  INPUT=inputRois, $
  NUM_ROIS=numRois, $
  OUTPUT=outputRois
  compile_opt idl2

  foreach roi, inputRois do begin
    if (~isa(roi, 'ENVIROI')) then begin
      Message, 'INPUT_ROIS element is not an ENVIROI'
    endif
  endforeach
  
  if (~Isa(inputRois, /ARRAY)) then begin
    Message, 'INPUT_ROIS should be an ARRAY'
  endif

  if (Isa(inputRois, 'Collection')) then begin
    Message, 'INPUT_ROIS is a collection, but it should not be'
  endif
  
  n = N_ELEMENTS(inputRois)
  if (numRois ne n) then begin
    Message, 'INPUT_ROIS is not of expected dimensions. IS: ' + $
      (n.ToString()).Join(',') + ' EXPECT:' + $
      (numRois.ToString()).Join(',')
  endif
  
  outputRois = inputRois
end
 