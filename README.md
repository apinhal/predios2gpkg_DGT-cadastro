# predios2gpkg

**convert DGT-cadastro-CGPR json to geopackage**

## run 
```shell
predios2gpkg.py <url>

predios2gpkg.py "https://snic.dgterritorio.gov.pt/geoportal/dgt_cadastro/api/v1/cadastro/cgpr/predios?dico=1214&dicofre=121411&seccao=C"
```

## +info:
- <https://www.dgterritorio.gov.pt/cadastro>
- <https://snic.dgterritorio.gov.pt/visualizadorCadastro>

```shell
# DGT-cadastro-CGPR json:
curl -s 'https://snic.dgterritorio.gov.pt/geoportal/dgt_cadastro/api/v1/cadastro/cgpr/predios?dico=1214&dicofre=121411&seccao=C'
```
