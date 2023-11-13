restricoes = ['AÇO', 'AMIANTO', 'BIAX', 'CERÂMICA', 'CHUMBO', 'COBRE', 'CONCRETO', 'DEFOFO', 'FOFO', 'FOGO', 'FIBRA PRFV', 'PEAD', 'PVC BRANCO', 'PVC PBA', 'PVC SOLDÁVEL', 'PVC ESGOTO CORRUGADO', 'PVC ESGOTO LISO', 'DESCONHECIDO']


len_rest = len(restricoes)
c = 0
when_c = 0
not_found = []

query = '''UPDATE rede_esgoto SET rde_material_nova = CASE
    WHEN LOWER(rde_material) = "aco" THEN "AÇO"::rde_material_enum
    WHEN LOWER(rde_material) = "amianto" THEN "AMIANTO"::rde_material_enum
    WHEN LOWER(rde_material) = "biax" THEN "BIAX"::rde_material_enum
    WHEN LOWER(rde_material) = "ceramica" THEN "CERÂMICA"::rde_material_enum
    WHEN LOWER(rde_material) = "chumbo" THEN "CHUMBO"::rde_material_enum
    WHEN LOWER(rde_material) = "cobre" THEN "COBRE"::rde_material_enum
    WHEN LOWER(rde_material) = "concreto" THEN "CONCRETO"::rde_material_enum
    WHEN LOWER(rde_material) = "defofo" THEN "DEFOFO"::rde_material_enum
    WHEN LOWER(rde_material) IN ("fofo", "ferro fundido") THEN "FOFO"::rde_material_enum
    WHEN LOWER(rde_material) = "ferro galvanizado" THEN "FOGO"::rde_material_enum
    WHEN LOWER(rde_material) = "fibra prfv" THEN "FIBRA PRFV"::rde_material_enum
    WHEN LOWER(rde_material) = "pead" THEN "PEAD"::rde_material_enum
    WHEN LOWER(rde_material) = "pvc branco" THEN "PVC BRANCO"::rde_material_enum
    WHEN LOWER(rde_material) = "pvc pba" THEN "PVC PBA"::rde_material_enum
    WHEN LOWER(rde_material) = "pvc soldavel" THEN "PVC SOLDÁVEL"::rde_material_enum
    WHEN LOWER(rde_material) IN ("pvc esgoto corrugado", "PVC.E.C") THEN "PVC ESGOTO CORRUGADO"::rde_material_enum
    WHEN LOWER(rde_material) IN ("pvc esgoto liso", "PVC.E.L") THEN "PVC ESGOTO LISO"::rde_material_enum
END;
'''

for restricao in restricoes:
  if query.find(restricao) != -1:
    print(query.find(restricao))
    c+=1
    if query.find("WHEN"):
      when_c +=   1
  else:
    not_found.append(restricao)

print(f"{c} {len_rest}")
print(not_found)
print(when_c)
print(query[382:])