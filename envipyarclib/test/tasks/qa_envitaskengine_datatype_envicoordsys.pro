;+
; :Description:
;    Task to test ENVI task engine of ENVICoordSys datatype
;    See qa_envitaskengine_datatype_envicoordsys.task for details
;       
; :Author:
;    JWD, October, 2015 - Initial Draft
;-
pro qa_envitaskengine_datatype_envicoordsys, INPUT=input, $
                                           OUTPUT=output
                                   
  compile_opt idl2
  
  expectType = 'ENVICoordSys'
  
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
