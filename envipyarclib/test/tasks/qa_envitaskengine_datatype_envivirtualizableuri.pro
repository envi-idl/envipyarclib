;+
; :Description:
;    Task to test task engine ENVIVIRTUALIZABLEURI datatype
;    See qa_envitaskengine_datatype_envivirtualizableuri.task for details
;       
; :Author:
;    MAJ, November, 2017 - Initial Draft
;-
pro qa_envitaskengine_datatype_envivirtualizableuri, INPUT=input, $
                                   OUTPUT=output
                                   
  compile_opt idl2
    
  expectType = 7
  
  isType = Size(input,/TYPE)
  if (isType NE expectType) then begin
    Message, 'INPUT is not of expected type. IS: ' + $
      String(isType) + 'EXPECT: ' + String(expectType)
  endif

  if (~Isa(input, /SCALAR)) then begin
    Message, 'INPUT is not a scalar'
  endif
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be'
  endif
  
  output = input

end
