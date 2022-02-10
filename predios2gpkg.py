#!/usr/bin/env python

# convert DGT-cadastro JSON to GeoPackage
# run: predios2gpkg.py <url>

""" 
+info:
https://www.dgterritorio.gov.pt/cadastro
https://snic.dgterritorio.gov.pt/visualizadorCadastro

run:
predios2gpkg.py "https://snic.dgterritorio.gov.pt/geoportal/dgt_cadastro/api/v1/cadastro/cgpr/predios?dico=1214&dicofre=121411&seccao=C"
"""

import sys, os
import requests, json
try:
  from osgeo import ogr,osr
except:
  import ogr, osr

# read JSON
#response = requests.get("https://snic.dgterritorio.gov.pt/geoportal/dgt_cadastro/api/v1/cadastro/cgpr/predios?dico=1214&dicofre=121411&seccao=C")
response = requests.get(sys.argv[1])
predios = json.loads(response.text)

# gpkg output
#gpkgFile = "predios.gpkg"
gpkgFile = predios[0]["dicofre"] + "-" + predios[0]["seccao"] + ".gpkg"
driver = ogr.GetDriverByName("GPKG")
if os.path.exists(gpkgFile):
    driver.DeleteDataSource(gpkgFile)
dataSource = driver.CreateDataSource(gpkgFile)
## set EPSG:3763 CRS
srs = osr.SpatialReference()
srs.ImportFromEPSG(3763)
## create polygon layer
layer = dataSource.CreateLayer(gpkgFile, srs, ogr.wkbPolygon)
## create layer attributes fields
layer.CreateField(ogr.FieldDefn("dicofre", ogr.OFTString))
layer.CreateField(ogr.FieldDefn("prd", ogr.OFTString))
layer.CreateField(ogr.FieldDefn("area", ogr.OFTInteger))


for predio in predios:
    # JSON fields
    #dicofre = predio["dicofre"]
    #prd     = predio["prd"]
    #area    = predio["area_m2"]
    wkt     = predio["wkt"]
    
    # create feature
    feature = ogr.Feature(layer.GetLayerDefn())
    # set feature attributes from json
    feature.SetField("dicofre", predio["dicofre"])
    feature.SetField("prd",     predio["prd"])
    feature.SetField("area",    predio["area_m2"])
    # set feature geometry (polygon) from Well Known Txt
    feature.SetGeometry(ogr.CreateGeometryFromWkt(wkt))
    layer.CreateFeature(feature)
    feature.Destroy()

# save and close data source
dataSource.Destroy()
