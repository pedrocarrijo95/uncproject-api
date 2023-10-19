from UncSoftwareAPI import unc_funcs as unc

code = "unc.getEstoque('0000000001')"
contexto = {'entidade': entidade}
exec(code,globals(),contexto)



#return contexto.get("resposta")