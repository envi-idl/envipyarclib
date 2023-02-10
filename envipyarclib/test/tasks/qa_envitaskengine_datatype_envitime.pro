;+
; :Description:
;    Task to test ENVI task engine of ENVITime datatype
;    See qa_envitaskengine_datatype_envitime.task for details
;       
; :Author:
;    MAJ, February, 2015 - Initial Draft
;-
pro qa_envitaskengine_datatype_envitime, INPUT=input, $
                                         OUTPUT=output
                                   
  compile_opt idl2
  
  expectType = 'ENVITIME'
  
  if (~Isa(input, expectType)) then begin
    Message, 'INPUT is not of expected type. IS: ' + $
      Typename(input) + 'EXPECT: ' + String(expectType)
  endif

  if (~Isa(input, /SCALAR)) then begin
    Message, 'INPUT is not a scalar'
  endif
  
  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be'
  endif
  
  output = input
  
end
