;+
; :Description:
;    Task to test task engine ENVIRasterSeries datatype
;    See qa_envitaskengine_datatype_envirasterseries.task for details
;
; :Author:
;    JWD, July, 2018 - Initial Draft
;-
pro qa_envitaskengine_datatype_envirasterseries, INPUT=input, OUTPUT=output
  compile_opt idl2

  if (~Isa(input, 'ENVIRasterSeries')) then begin
    Message, 'INPUT is not an ENVIRasterSeries'
  endif

  if (Isa(input, /ARRAY)) then begin
    Message, 'INPUT must be scalar'
  endif

  if (Isa(inputRois, 'Collection')) then begin
    Message, 'INPUT is a collection'
  endif

  output = input
end
