# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# python.py
# Created on: 2021-12-20 14:16:34.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Polygons = "Polygons"
Polygons_1 = "Polygons_1"
ok_shp = "H:\\IGIS\\IGIS SEM 5\\GIS Applications Lab\\toolmaking\\ok1.shp"

# Process: Merge
arcpy.Merge_management("Polygons;Polygons_1", ok_shp, "Name \"Name\" true true false 254 Text 0 0 ,First,#,Polygons,Name,-1,-1,Polygons_1,Name,-1,-1;FolderPath \"FolderPath\" true true false 254 Text 0 0 ,First,#,Polygons,FolderPath,-1,-1,Polygons_1,FolderPath,-1,-1;SymbolID \"SymbolID\" true true false 10 Long 0 10 ,First,#,Polygons,SymbolID,-1,-1,Polygons_1,SymbolID,-1,-1;AltMode \"AltMode\" true true false 5 Long 0 5 ,First,#,Polygons,AltMode,-1,-1,Polygons_1,AltMode,-1,-1;Base \"Base\" true true false 19 Double 0 0 ,First,#,Polygons,Base,-1,-1,Polygons_1,Base,-1,-1;Clamped \"Clamped\" true true false 5 Long 0 5 ,First,#,Polygons,Clamped,-1,-1,Polygons_1,Clamped,-1,-1;Extruded \"Extruded\" true true false 5 Long 0 5 ,First,#,Polygons,Extruded,-1,-1,Polygons_1,Extruded,-1,-1;Snippet \"Snippet\" true true false 254 Text 0 0 ,First,#,Polygons,Snippet,-1,-1,Polygons_1,Snippet,-1,-1;PopupInfo \"PopupInfo\" true true false 254 Text 0 0 ,First,#,Polygons,PopupInfo,-1,-1,Polygons_1,PopupInfo,-1,-1;Shape_Leng \"Shape_Leng\" true true false 19 Double 0 0 ,First,#,Polygons,Shape_Leng,-1,-1,Polygons_1,Shape_Leng,-1,-1;Shape_Area \"Shape_Area\" true true false 19 Double 0 0 ,First,#,Polygons,Shape_Area,-1,-1,Polygons_1,Shape_Area,-1,-1")

