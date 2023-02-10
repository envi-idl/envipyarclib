;+
; :Description:
;    Task to test ENVI task engine of ENVIRASTERSERIESARRAY datatype
;    See qa_envitaskengine_datatype_envirasterseriesarray.task for details
;       
; :Author:
;    JWD, July, 2018 - Initial Draft
;-
pro qa_envitaskengine_datatype_envirasterseriesarray, INPUT=input, SIZE=size, $
  OUTPUT=output                            
  compile_opt idl2
  
  if (~Isa(input, /ARRAY)) then begin
    Message, 'INPUT is not an array'
  endif
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be'
  endif
  
  actualSize = N_ELEMENTS(input)
  if (size ne actualSize) then begin
    Message, 'INPUT is not of expected size. IS: ' + $
      STRTRIM(actualSize, 2) + ' EXPECT: ' + STRTRIM(size, 2)
  endif
  
  expectType = 'ENVIRASTERSERIES'
  foreach series, input do begin
    if (~Isa(series, expectType)) then begin
      Message, 'INPUT is not of expected type. IS: ' + $
        Typename(input) + 'EXPECT: ' + String(expectType)
    endif
  endforeach
  
  output = input
end
